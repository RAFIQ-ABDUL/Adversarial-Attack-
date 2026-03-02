# Adversarial Attack Assessment (FGSM)

This project demonstrates a Fast Gradient Sign Method (FGSM) adversarial attack on a pretrained MNIST image classification model. It includes a FastAPI backend deployed on AWS EC2 and a web frontend deployed on AWS Amplify.

## Deployed URLs

* **Frontend (AWS Amplify):** `[https://staging.d17i5ypwk66sej.amplifyapp.com/]`
* **Backend API (AWS EC2 t3.micro):** `http://13.62.100.170:8000/docs`

> **⚠️ IMPORTANT TESTING NOTE (Mixed Content Bypass):** > Because the frontend is hosted securely on AWS Amplify (`https://`) and the backend is hosted on a Free Tier AWS EC2 instance without an SSL certificate (`http://`), modern web browsers will automatically block the API requests by default due to standard Mixed Content security rules. 
> 
> **To test the live application:** You must test it on a desktop browser. In Google Chrome:
> 1. Click the Site Information icon (the tuning-fork/padlock) on the far left of your URL address bar.
> 2. Go to **Site Settings**.
> 3. Scroll to **Insecure Content** and change the dropdown from "Block (default)" to **Allow**.
> 4. Reload the page. The frontend will now successfully communicate with the EC2 backend.

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
   (Note: Ensure the fetch URL in the JavaScript inside index.html points to http://127.0.0.1:8000/attack instead of the live EC2 IP for local testing).

Explanation of FGSM:

The Fast Gradient Sign Method (FGSM) is a adversarial attack designed to trick neural networks into misclassifying an image. During normal training, a model uses gradient descent to adjust its internal weights to minimize the loss function. FGSM flips this concept: it uses the gradients of the loss function with respect to the input image itself to mathematically maximize the loss.By extracting the sign of these input gradients, the attack determines exactly which direction to change the pixel values to cause the most confusion for the model. This calculated directional noise is then multiplied by a small constraint factor called epsilon and added to the original image. The result is an image that looks visually identical to the human eye but completely shatters the neural network's confidence. This in return decreases the robustness.

Observation:

Prediction Changes: The model successfully classified clean MNIST digits with high confidence. However, once the FGSM perturbation was applied, the model's prediction consistently flipped to an entirely incorrect class, demonstrating the fragility of the standard neural network against mathematically calculated noise.
