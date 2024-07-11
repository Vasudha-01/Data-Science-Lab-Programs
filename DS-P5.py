#!/usr/bin/env python
# coding: utf-8

# In[ ]:


iris = load_iris()
X = iris.data
y = iris.target


# In[ ]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# In[ ]:


kernels = ['rbf']
gammas = [0.5]
Cs = [0.01, 1, 10]
best_accuracy = 0
best_parameters = None
best_support_vectors = None


# In[ ]:


for kernel in kernels:
    for gamma in gammas:
        for C in Cs:
            svm_clf = SVC(kernel=kernel, gamma=gamma, C=C, decision_function_shape='ovr')
            svm_clf.fit(X_train, y_train)


# In[ ]:


y_pred = svm_clf.predict(X_test)


# In[ ]:


accuracy = accuracy_score(y_test, y_pred)


# In[ ]:


total_support_vectors = np.sum(svm_clf.n_support_)


# In[ ]:


print(f"Kernel: {kernel}, Gamma: {gamma}, C: {C}, Accuracy: {accuracy}, Total Support Vectors: {total_support_vectors}")


# In[ ]:


if accuracy > best_accuracy:
    best_accuracy = accuracy
    best_parameters = (kernel, gamma, C)
    best_support_vectors = total_support_vectors


# In[ ]:


print("\nBest Classification Accuracy:", best_accuracy)
print("Best Hyperparameters:", best_parameters)
print("Total Support Vectors for Best Model:", best_support_vectors)

