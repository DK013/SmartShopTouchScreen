from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from psycopg2.extensions import AsIs
import psycopg2
from psycopg2.extras import DictCursor
import datetime
from decimal import Decimal


class SqlTableModel(QAbstractTableModel):
    def __init__(self, connection, tableName = None, columnSortName = None, columnSortOrder = None, filter = None,
                 filterArgs = [], fields = None, displayColumnMapping = None, parent = None):
        super(SqlTableModel, self).__init__(parent)

        self.tableName = tableName
        self.columnSortName = columnSortName
        self.columnSortOrder = columnSortOrder
        self.filter = filter
        self.filterArgs = filterArgs
        self.fields = fields
        self.displayColumnMapping = displayColumnMapping

        self.connection = connection
        # Create cursor for SqlTableModel
        self.cursor = self.connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        self.resdata = []
        self.header = []

        # Execute the select statement if a table name was given
        if tableName is not None:
            self.select()

    def select(self):
        sql = self.selectStatement(False)
        if sql is None:
            return False

        self.beginResetModel()
        self.cursor.execute(sql, self.filterArgs)

        self.resdata = self.cursor.fetchall()
        self.header = [desc[0] for desc in self.cursor.description]
        self.endResetModel()
        return True

    def setTable(self, name):
        try:
            self.cursor.execute("SELECT * FROM %s", (AsIs(name),))
            self.cursor.fetchall()
            self.tableName = name
        except psycopg2.Error:
            print('Invalid table name %s' % name)

        # Commit connection in case an exception occurred
        self.connection.commit()

    def setSort(self, column, order):
        self.columnSortName = column
        self.columnSortOrder = order

    def setFilter(self, filter, filterArgs = []):
        self.filter = filter
        self.filterArgs = filterArgs

    # Contains a list of column names that the query should retrieve. If None, then set to all columns (*)
    def setFields(self, fields):
        self.fields = fields

    def setDisplayColumnMapping(self, displayColumnMapping):
        self.displayColumnMapping = displayColumnMapping

    def getSelectedRecord(self, index):
        if not index.isValid() and index.row() >= len(self.resdata):
            return None

        return self.resdata[index.row()]

    def getSelectedRecords(self, indexes):
        records = []
        for index in indexes:
            if index.isValid() and index.row() < len(self.resdata):
                records.append(self.resdata[index.row()])

        return records

    def selectStatement(self, runTwice = True):
        if self.tableName is None:
            print('No table name. Cannot get select statement')
            return None

        filter = ''
        orderByClause = ''
        fields = ''

        if self.filter is not None:
            filter = ' WHERE ' + self.filter

        if self.columnSortName is not None and self.columnSortOrder is not None:
            orderByClause = ' ORDER BY ' + self.columnSortName
            orderByClause += (' ASC' if self.columnSortOrder == Qt.AscendingOrder else ' DESC')

        if self.fields is None:
            fields = '*'
        else:
            fields = ','.join(self.fields)

        # Run through the statement once. Run it through again because the filter string might have additional arguments
        # to add in (filterArgs)
        firstRun = self.cursor.mogrify("SELECT %s FROM %s%s%s", (AsIs(fields), AsIs(self.tableName), AsIs(filter),
                                                               AsIs(orderByClause)))

        if runTwice:
            return self.cursor.mogrify(firstRun, self.filterArgs)
        else:
            return firstRun

    def rowCount(self, parent = None):
        return len(self.resdata)

    def columnCount(self, parent = None):
        return len(self.header)

    def data(self, index, role = None):
        if role != Qt.DisplayRole:
            return None

        columnIndex = index.column() if self.displayColumnMapping is None else self.displayColumnMapping[index.column()]
        val = self.resdata[index.row()][columnIndex]

        if val is None:
            return None
        elif isinstance(val, Decimal):
            # make sure to convert special classes (otherwise it is user type in QVariant)
            return str(val)
        elif isinstance(val, datetime.datetime):
            return str(val)
        else:
            return val

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None

        if orientation == Qt.Vertical:
            # header for a row
            return section + 1
        else:
            # header for a column
            return self.header[section] if self.displayColumnMapping is None else self.header[self.displayColumnMapping[section]]