from flask import Flask, request, render_template_string
from openai import OpenAI
import os

app = Flask(__name__)

# OpenAI API key from Render Environment Variables
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Automated RTI Info Assistant</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f2f2f2;
            margin: 0;
            padding: 40px;
        }

        .container {
            max-width: 700px;
            margin: auto;
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 0 10px #ccc;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        p {
            text-align: center;
            color: #666;
        }

        textarea {
            width: 100%;
            height: 120px;
            padding: 12px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 8px;
            font-size: 16px;
            resize: vertical;
        }

        button {
            margin-top: 15px;
            width: 100%;
            padding: 12px;
            background: #333;
            color: white;
            border: none;
            border-radius: 8px;
            font-size: 16px;
            cursor: pointer;
        }

        button:hover {
            background: #555;
        }

        .answer {
            margin-top: 25px;
            padding: 20px;
            background: #f5f5f5;
            border-radius: 8px;
            line-height: 1.6;
        }
    </style>
</head>

<body>

<div class="container">

    <h1>Automated RTI Info Assistant</h1>

    <p>Ask your question about the Right to Information (RTI) Act.</p>

    <form method="POST">

        <textarea
            name="question"
            placeholder="Example: How can I file an RTI?"
            required
        ></textarea>

        <button type="submit">
            Ask RTI Assistant
        </button>

    </form>

    {% if answer %}
    <div class="answer">
        <strong>RTI Assistant:</strong>
        <p>{{ answer }}</p>
    </div>
    {% endif %}

</div>

</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():

    answer = ""

    if request.method == "POST":

        question = request.form.get("question", "").strip()

        if question:

            prompt = f"""
You are an Automated RTI Information Assistant for India.

Your purpose is to provide simple educational information about
the Right to Information Act, 2005.

You can explain:
- What is RTI?
- How to file an RTI application
- RTI application format
- Public Information Officer (PIO)
- RTI fees
- RTI response time
- First Appeal
- Second Appeal
- Basic RTI procedure

Rules:
1. Give simple and clear answers.
2. Use easy language suitable for students and citizens.
3. Do not claim to be a government officer.
4. Do not invent laws, rules, fees, deadlines, or government information.
5. If the question requires current official information, advise the user
   to verify it with the relevant official government RTI source.
6. This assistant provides information and is not a substitute for
   professional legal advice.

User Question:
{question}
"""

            try:

                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=prompt
                )

                answer = response.output_text

            except Exception as e:

                answer = "Sorry, an error occurred. Please check the API key and try again."

    return render_template_string(
        HTML,
        answer=answer
    )


@app.route("/health")
def health():
    return "Automated RTI Info Assistant is running!"


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port
    )
