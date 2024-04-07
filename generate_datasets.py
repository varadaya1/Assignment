import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

# Prepare data
X = np.array([[0.11112997, 0.62854347],
              [0.21625375, 0.18931446],
              [0.12897503, 0.84651514],
              [0.73714453, 0.61876454],
              [0.3047579,  0.73799038]])
y = np.array([0, 0, 0, 1, 0])

# Convert data to PyTorch tensors
X_tensor = torch.tensor(X, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.float32)

# Define logistic regression model
class LogisticRegression(nn.Module):
    def __init__(self, input_size):
        super(LogisticRegression, self).__init__()
        self.linear = nn.Linear(input_size, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out = self.linear(x)
        out = self.sigmoid(out)
        return out

# Initialize model, loss function, and optimizer
model = LogisticRegression(input_size=X.shape[1])
criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Training loop
num_epochs = 1000
for epoch in range(num_epochs):
    # Forward pass
    outputs = model(X_tensor)
    loss = criterion(outputs.squeeze(), y_tensor)

    # Backward and optimize
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if (epoch+1) % 100 == 0:
        print(f'Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item():.4f}')

# Evaluate model
with torch.no_grad():
    predicted = model(X_tensor).squeeze().round().numpy()
    accuracy = (predicted == y).mean()
    print(f'Accuracy: {accuracy:.4f}')
