# from causalinference import CausalModel
# from causalinference.utils import random_data
# 
# Y, D, X = random_data()
# causal = CausalModel(Y, D, X)
# 
# print(causal)
# print(Y)


from sklearn import datasets

iris = datasets.load_iris()
digits = datasets.load_digits()

#print(iris)
print(digits.data)