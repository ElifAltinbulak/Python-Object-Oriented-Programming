from datetime import datetime
class Date:
    def __init__(self,month,b_date,year):
        self.date = b_date
        self.month = month
        self.year = year
    def __str__(self):
        return "%s/%s/%s" %(self.date,self.month,self.year)
    def getmonth(self):
        return self.month
class Employee:
    def __init__( self, first, last , Date , departmentCode ):
        if self.__class__ == Employee:
            raise NotImplementedError("Cannot create object of class Employee")
        self.firstName = first
        self.lastName = last
        self.birthDate = Date
        self.departmentCode = departmentCode
    def __str__( self ):
        return "%s %s" % ( self.firstName, self.lastName )
    def _checkPositive( self, value ):
        if value < 0:
            raise ValueError("Attribute value (%s) must be positive" % value)
        else:
            return value
    def earnings( self ):
        raise NotImplementedError("Cannot call abstract method")
class Boss( Employee ):
    def __init__( self,first, last, salary ,Date, department ):
        Employee.__init__( self, first, last , Date, department )
        self.weeklySalary = self._checkPositive( float( salary ) )
    def earnings( self ):
        return self.weeklySalary
    def __str__( self ):
        return "%17s: %s" % ( "Boss", Employee.__str__( self ) )
class CommissionWorker( Employee ):
    def __init__( self, first, last, salary, commission, quantity ,Date, department ):
        Employee.__init__( self, first, last, Date, department )
        self.salary = self._checkPositive( float( salary ) )
        self.commission = self._checkPositive( float( commission ) )
        self.quantity = self._checkPositive( quantity )
    def earnings( self ):
        return self.salary + self.commission * self.quantity
    def __str__( self ):
        return "%17s: %s" % ( "Commission Worker",
            Employee.__str__( self ) )
class PieceWorker( Employee ):
    def __init__( self, first, last, wage, quantity , Date, department ):
        Employee.__init__( self, first, last, Date, department )
        self.wagePerPiece = self._checkPositive( float( wage ) )
        self.quantity = self._checkPositive( quantity )
    def earnings( self ):
        return self.quantity * self.wagePerPiece
    def __str__( self ):
        return "%17s: %s" % ( "Piece Worker",
            Employee.__str__( self) )
class HourlyWorker( Employee ):
    def __init__( self, first, last, wage, hours , Date, department ):
        Employee.__init__( self, first, last, Date, department )
        self.wage = self._checkPositive( float( wage ) )
        self.hours = self._checkPositive( float( hours ) )
    def earnings( self ):
        if self.hours <= 40:
            return self.wage * self.hours
        else:
            return 40 * self.wage + ( self.hours - 40 ) *\
                self.wage * 1.5
    def __str__( self ):
        return "%17s: %s" % ( "Hourly Worker",
            Employee.__str__( self ) )
currentMonth = datetime.now().month
employees = [ Boss( "John", "Smith", 800.00 ,Date(5,11,1984),'D1'),
            CommissionWorker( "Sue", "Jones", 200.0, 3.0, 150 ,Date(6,15,1988),'D2'),
            PieceWorker( "Bob", "Lewis", 2.5, 200 ,Date(6,25,1985),'D3'),
            HourlyWorker( "Karen", "Price", 13.75, 40,Date(9,27,1978),'D4' ) ]
for employee in employees:
    bonus = 0
    if currentMonth == employee.birthDate.getmonth():
        bonus = 100
    print ("%s earned $%.2f" %(employee, employee.earnings()+bonus))
© 2021 GitHub, Inc.
