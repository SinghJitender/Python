from OwnModuleCall import func
print("Inside CallOwnModule")
func()

from MethodsAndFunctions import Functions
print(Functions.pig_latin("ABCD"))

from ModulesAndPackages.SubPackage import DummySubFile as d
d.dummyMethod()

