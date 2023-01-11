import os
import openai

openai.organization = "org-SnJuzBNRF165j7NQuxaxFDwa"
openai.api_key = "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"



def get_response(message: str) -> str:
    """ resp = api.send_message(message)
    print(resp['message']) 
    return resp['message'] """
    

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message,
        max_tokens=100,
        temperature=0,

    )
    choices = response["choices"]
    response = choices[0]["text"]
    # print(response)
    return response

from pyChatGPT import ChatGPT

session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..jeMT7PKY689ghDhI.21DJzeYYlnAkb84OYJlPTUiBx_5Mjiu6ulTXkEuu_WhMo-V3gt7lLnrwAJKMSPgh055eduIJKWmFz3sIQzjO031VMHdp-fofOaDMZfS6axM7OAPL9E8dWV1YyOEMoxjusxvi_HYS81lBfX41psfEpoM3cNVHqFx-7oeSKbeJDX5tR__GSbiNasOLtYUbAZPE6k6VwiuxWWRptmIb-aBD4qC8OgMTF5DTTcNQlRq3BSZg5I8OEDEN6KjLPt382kJvr3JbJGWnBrsxoqqPS5p076trOt99SW9YQOBLkhuEwoA1YlCGhNTYkW4YDNZjsaDNl2Pc193Uvn2wpfF9q4uwIpYNVpwNSCHWgO5hoFMKv54c8jXKGNpmkkkxuCMdCwGNilmEY7iGUUUwqu3K_0wvkeNPlNrzIJ5m5gf77Ap-JOoV0I--nMuOZoPZLp-T6t4D4r7CR-KregvznOMH-gwTPv-7LAFffZW3oSvhrMMDwcLzYow-aQM-5soK1uKnrRBB3s3sYIeZTDqm6EF7uZL7diymjV70xM0KFVNLcswNplwUy-W8NRAigiuYB4JkwDGw5Qh9VWqALKviN2yzoqM3f2KUtOaV8tAHMqj51yApZNxoBEpRV6uFo6DG6TSDN12S5ynibzJZ98ZYLI2GF3YWtTKuGmWESI7tnzZQ-vcCkwg1zlikdiz3RvzlPaEotelOZNGQkjYEfNrFiuC9IfGe-6p9MzBlYTJrunSteP9fGbz5wigPIKkBBwkFT2taSuEFWzCs8Ac-z5T3GakvQzADMbRa0rHpzfHXlOC_1X8_Noo5KGZ5z7XeQLhzauAf_1MCQDwO6gZ98McC-IZyqRbC5uLmBxar4kAAXlbVV9kitn0CH-6yb0ZOyO4V5XR4NXQmg0VZ648vPH_bIRbMpDXpFpSLjugiJTZeogJXUsq-cQYPJbvcPHc9dyJrq29l0tMWcy3wTn1ZKRmQpG_SB08tKt8D2iR0tRRD04QiH9Wj515JHOhWH-FOcffkv3KXCEORZ_CAqw3eMShhB2Mj3qvbW3TkniJivJ7jiBTEm0gZjkVME_V78ROe-acb4VCYqyCmqqKKe1dXXoPCWlKoCnYQCMJP4O3o6QqgJ8nVfuXdor63iOGzHG3dhEeJxSKrYPaHO7X8762aYQ-pjIyvo61JvCobtEjvWEZpN6h-Rm6g_-sANPjI04-ytn2mzGn_OunBRT_GA_tT2qA87tPGhV5Ugltc3q2-XA4yayUR6R-nELSn4E7lbDnpLIQbBrhFtcG-IP4PdzmToGNnpL7rlBZueU4B2UrlAb29TsOl7etv-JKx_fGhsAYF5TBjLN0GUml1VeGEfajJp5hqCCruudI2h0w9TWydB3d3qlggakBt7B1tqQlU3inYE6TxDRPuIuJ9iCLGMFFufMfiTPPgBchrh3J697rbBfcws4L72dsNuH4ydRkXSEk8RcwvC0bpOSuSvWfsdHg7M2CNE5l2Xb4JaWfEN9UzBIyHL6_mPOIIZSuGmNepXcf_PxmQsDeM-EMBTBjGESaPZR5JvXpYZxqNm6PMY8ker049Nw7opvzl6wAhnOkJHzLl16orV-p5qce1aJCDXff-LT9cVjIefd_KHjsMsus7p6yT-rsz60r73ww0Ifvxr4ptw9W7Txg2V38qVls8WoX7YaJdiO5NzLanhT_Oi0wJGvy2zNBXTbYcRAFWQNCgdmFrwrUzM3wFDk5kwp3uVOSe_GtvuHqxH01j6P7SoQyxn7mJVInyKtAbSoLrFwqIPtdBazhdQrOCEwkIK8KUnr_50tkBORBJxoFe_yIPCNmwUhj69vNYwz_WGOnERwTnJL5YmMSgLlJIBWB4-0gswZQi0CYAlAUFaWrtaRx06MPZvBogWgHZ8D1i4IO1DCatEKnSDUzvKO_7WiCroHcX5HabcNjwwt-rNzLiofNspF-ptYksf0yL51lUH5i7vSWyqjs2lVRWj_Q8nLMv-EfTwPo8yyJnC8G5rMmfoUhjeDE-HI274c8l00RthAWxxzCeueP0rM4wSYOtWrmqp3R6QAVqfUDd2y-P10RMG1oQB3S0HH_uv1GfGmEtALp9o2zHm-eXOTQUtY63FkSAwHePw6zVYw9jm7DvWYIIn_Kxaqi6GEZmw1mwrlGyMZ6rHF5q_aLpDL8fHSQ5ph-CNYVNjv-UmGGMVRZvDXrifabXKhKYHVoK2LoUAiShGkYFxsckxbX8tcx33BsMZWvsd_RJK16EKgVKlzMi8UdGis6yqFoU5rleJ80CKJt7Ci-lFELo7rTI0M8.YxLxmvZ5wHZqOqaUxNzhnQ' 

api = ChatGPT(session_token) 
""" from pychatgpt import Chat

# Create a Chat object
chat = Chat(email="senpaireymes@gmail.com", password="senpaireymes@gmail.com", 
            conversation_id="Parent Conversation ID", 
            previous_convo_id="Previous Conversation ID")

answer, parent_conversation_id, conversation_id = chat.ask("How are you?")

print(answer)

# Or change the conversation id later
answer, _, _ = chat.ask("How are you?", 
                        previous_convo_id="Parent Conversation ID",
                        conversation_id="Previous Conversation ID")
print(answer) """