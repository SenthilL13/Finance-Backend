import joblib
from dataset import menu, questions_data, answers_data, exit_message, Other_mutualFunds
from difflib import get_close_matches

# Load trained model for follow-up question prediction
FOLLOWUP_MODEL_PATH = r"D:\Freelancing Projects\FINO_ChatBot\followup_model.pkl"
VECTORIZER_PATH = r"D:\Freelancing Projects\FINO_ChatBot\followup_vectorizer.pkl"

try:
    followup_model = joblib.load(FOLLOWUP_MODEL_PATH)
    followup_vectorizer = joblib.load(VECTORIZER_PATH)
except FileNotFoundError as e:
    print(f"Error: {e}")
    followup_model, followup_vectorizer = None, None  # Prevent crash if files are missing


def fn_chatbot_welcome(request):
    try:
        return {
            "id": 0,
            "message": "Hi! Welcome !!\nI'm Fino, your very own personal assistant.\n"
                       "I can help you with your queries. Ask me more by choosing one of the options below.",
            "Questions": menu
        }
    except Exception as e:
        return {"error": f"Exception in fn_chatbot_welcome: {str(e)}"}


def fn_chat_assist(request):
    """ Handles category selection, answering questions, and navigating menu. """
    try:
        qn_id = int(request.get("id"))

        # Handle Main Menu Request
        if qn_id == 0:
            return {
                "id": 0,
                "message": "You are now back at the main menu. Please select a category:",
                "Questions": menu
            }

        # Handle Exit Request
        if qn_id == -1:
            return {
                "id": -1,
                "message": exit_message,
                "Questions": [{"id": 0, "question": "Restart Chat"}, {"id": -1, "question": "Exit"}]
            }

        if qn_id == 7:
            return {
                "id": 7,
                "message":  Other_mutualFunds,
                "Questions": [{"id": 0, "question": "Restart Chat"}, {"id": -1, "question": "Exit"}]
            }

        # Handle Category Selection
        if qn_id in questions_data:
            category_name = next((item["question"] for item in menu if item["id"] == qn_id), "Unknown Category")
            return {
                "id": qn_id,
                "message": f"You selected '{category_name}'. Choose a question below:",
                "Questions": questions_data[qn_id]
            }

        # Handle Answer and Predict Follow-Up Questions
        if qn_id in answers_data:
            answer = answers_data[qn_id]

            # Find original question text
            question_text = next(
                (q["question"] for q_list in questions_data.values() for q in q_list if q["id"] == qn_id),
                None
            )

            followup_questions = []

            if followup_model and followup_vectorizer and question_text:
                # Predict possible follow-up question
                question_vector = followup_vectorizer.transform([question_text])
                predicted_question_text = followup_model.predict(question_vector)[0]

                # Find the 4 closest matches in predefined questions
                all_questions = [(q["id"], q["question"]) for q_list in questions_data.values() for q in q_list]
                closest_matches = get_close_matches(predicted_question_text, [q[1] for q in all_questions], n=4, cutoff=0.5)

                # Prepare follow-up questions list
                for match in closest_matches:
                    match_id = next(q[0] for q in all_questions if q[1] == match)
                    followup_questions.append({
                        "id": match_id,
                        "question": match,
                        "answer": answers_data.get(match_id, "No answer available.")
                    })

            # Return response with answer and multiple follow-up question options
            return {
                "id": qn_id,
                "answer": answer,
                "recommended_followups": followup_questions if followup_questions else "No related questions found.",
                "Questions": [{"id": 0, "question": "Main Menu"}, {"id": -1, "question": "Exit"}]
            }

        return {"message": "Invalid ID. Please select from the main menu."}

    except Exception as e:
        return {"error": f"Exception in fn_chat_assist: {str(e)}"}
