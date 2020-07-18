import pandas

dataFrame = pandas.DataFrame([[2,4,6],[3,5,7]], columns = ["Price", "Age", "Value"], index = ["First", "Second"])
print(dataFrame)
print(dataFrame.mean())
print(dataFrame.mean().mean())
print(dataFrame.Price.mean())
