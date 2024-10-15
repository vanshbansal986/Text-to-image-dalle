# 🎨 AI Generation Hub

AI Generation Hub is a Streamlit-based web application that leverages the power of OpenAI's DALL-E 3 and Hugging Face models to perform various AI-powered tasks, including text-to-image generation and image-to-text conversion.

## Features

- **Text to Image Generation (DALL-E)**: Generate images from text prompts using OpenAI's DALL-E 3 model.
  - Customizable image size, quality, and style.
- **Text to Image Generation (Stable Diffusion)**: Create images from text descriptions using the Stable Diffusion model.
  - Adjustable resolution and quality settings. Did not work because server couldnt handle the load.

## Installation

1. Clone this repository:
 

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Use the sidebar to select the desired task:
   - Text to Image (DALL-E)

4. Follow the on-screen instructions to input your text prompt or upload an image.

5. Click the "Generate" button to process your request.

6. View the results in the main content area.

## Requirements

- Python 3.7+
- Streamlit
- OpenAI API key
- PyTorch
- Transformers
- Diffusers
- Pillow
- python-dotenv

See `requirements.txt` for a full list of dependencies.

## Configuration

You can customize the app's behavior by modifying the following parameters in `app.py`:

- Available image sizes for DALL-E
- Quality options for both DALL-E and Stable Diffusion
- Resolution options for Stable Diffusion
- Model selection for Stable Diffusion and Image-to-Text tasks

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- OpenAI for the DALL-E 3 API
- Hugging Face for the Transformers and Diffusers libraries
- Streamlit for the web app framework

## Disclaimer

This application uses AI models that may produce content. Please use responsibly and in accordance with OpenAI's use-case policies and content guidelines.

