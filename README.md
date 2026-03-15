# Adversarial Attack Assessment (FGSM)

This project demonstrates a Fast Gradient Sign Method (FGSM) adversarial attack on a pretrained MNIST image classification model. It includes a FastAPI backend  and a web frontend deployed.

---

## How to Run Locally

### Backend Setup
1. Navigate to the `backend` directory in your terminal.
2. Create a Python virtual environment:
   ```bash
   python -m venv venv
3. Activate the environment:

   Windows: venv\Scripts\activate

   Mac/Linux: source venv/bin/activate

4. Install the required dependencies:

   pip install -r requirements.txt
5. Start the FastAPI server:
   uvicorn backend:app --host 127.0.0.1 --port 8000
6. Frontend Setup
   Open the frontend directory.
   Open the index.html file in any modern web browser.
   (Note: Ensure the fetch URL in the JavaScript inside index.html points to http://127.0.0.1:8000/attack).

Explanation of FGSM:

The Fast Gradient Sign Method (FGSM) is a adversarial attack designed to trick neural networks into misclassifying an image. During normal training, a model uses gradient descent to adjust its internal weights to minimize the loss function. FGSM flips this concept: it uses the gradients of the loss function with respect to the input image itself to mathematically maximize the loss.By extracting the sign of these input gradients, the attack determines exactly which direction to change the pixel values to cause the most confusion for the model. This calculated directional noise is then multiplied by a small constraint factor called epsilon and added to the original image. The result is an image that looks visually identical to the human eye but completely shatters the neural network's confidence. This in return decreases the robustness.

Observation:

Prediction Changes: The model successfully classified clean MNIST digits with high confidence. However, once the FGSM perturbation was applied, the model's prediction consistently flipped to an entirely incorrect class, demonstrating the fragility of the standard neural network against mathematically calculated noise.
