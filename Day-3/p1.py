import time
class Vendor:
    def __init__(self,vname,vGST):
        self.vname = vname
        self.vGST= vGST
        print(f'Vendor {self.vname} enrollment is done!')

    def billing(self,pName,pCost=0.0,pQty=0):
        self.pName =pName
        self.pCost = pCost
        self.pQty = pQty
        self.tax = 0.18
        self.total = self.pQty * self.pCost
        self.gs = self.total + self.tax
        

    def purchase_info(self):
        wobj = open("purchase_info.log", "w")
        wobj.write(f'{self.vname}\t{self.vGST}\t{self.pName}\t{self.pCost}')
        wobj.write(f'{self.pQty}\t{self.total}\t{self.gs}\tBilling date:{time.ctime()}\n\n')
        wobj.close()


vobj1 = Vendor('V-Abc', '1NAPLCG3423')
vobj2 = Vendor('V-Xyz', '4ZADFBER5')

vobj1.billing('prodA', 1000, 3)
vobj1.billing('prodB', 1200, 2)
vobj1.billing('prodC', 5000, 3)

vobj2.billing('prodY', 4213, 2)

vobj3 = Vendor('V-dab', 'F1231232o')

vobj3.billing('prodA', 1500,3)
vobj1.purchase_info()


'''      
obj1 = Vendor('ss','ss')
#obj1.__init__(obj1,'flipkart','tttt')
obj1.billing('lux')
'''
