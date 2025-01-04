from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from openai import OpenAI

client = OpenAI(api_key=settings.OPENAI_API_KEY)
@csrf_exempt
def bird_chatter(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_message = data.get("message", "").strip().lower()

        # ChatGPT response for general bird chat
        try:
                response = client.chat.completions.create(model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a nature conservationist who loves birds and their conservation. "
                            "You are especially focused on the following birds and their importance in nature:\n"
                            "- Satyr Tragopan\n- Swamp Francolin\n- Black-necked Crane\n- Spotted Dove\n- Wood Snipe\n"
                            "- Rufous-necked Hornbill\n- Common Pochard\n- Rose-ringed Parakeet\n- Black Kite\n"
                            "- Bristled Grassbird\n- House Crow\n- Indian Spotted Eagle\n- Spiny Babbler\n- Long-tailed Duck\n"
                            "- Sarus Crane\n- Rufous Treepie\n- Grey-crowned Prinia\n- House Sparrow\n- Kashmir Flycatcher\n"
                            "- Black-breasted Parrotbill\n- Himalayan Monal\n- Rustic Bunting\n- Grey-sided Thrush\n"
                            "- Egyptian Vulture\n- Eastern Imperial Eagle\n- Asian Koel\n- Common Cuckoo\n"
                            "- Swamp Grass Babbler\n- Common Wood Pigeon\n- Greater Spotted Eagle\n- Steppe Eagle\n"
                            "- Red-billed Blue Magpie\n- Cheer Pheasant\n- White-throated Bush Chat\n- Slender-billed Babbler\n"
                            "- Great Slaty Woodpecker\n- Pallas's Fish Eagle\n- Large-billed Crow\n- Grey Treepie\n"
                            "- Jerdon's Babbler\n- Saker Falcon.\n\n"
                            "You only discuss these birds weather it be its nepali name or not. If a user mentions any other topic, kindly redirect the conversation "
                            "back to these birds. Always encourage their conservation and raise awareness about their importance. "
                            "Always end your conversation with, 'Do you want a report?' If the user responds with 'yes,' generate "
                            "a detailed, well-researched document about the birds the user is interested in talking about."
                        )
                    },
                    {"role": "user", "content": data.get("message", "")},
                ])
                assistant_reply = response.choices[0].message.content
                return JsonResponse({"reply": assistant_reply})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)