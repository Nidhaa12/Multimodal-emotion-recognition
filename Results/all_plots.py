import matplotlib.pyplot as plt

models = ["Speech", "Text", "Fusion"]
accuracies = [100, 100, 100]

plt.figure(figsize=(8,5))

plt.bar(models, accuracies)

plt.ylim(0,100)

plt.xlabel("Models")
plt.ylabel("Accuracy (%)")
plt.title("Emotion Recognition Model Comparison")

plt.savefig("all_models_accuracy.png")

plt.show()