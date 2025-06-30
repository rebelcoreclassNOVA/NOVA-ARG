def start_nova_chat(decrypted_message):
    print("\nNOVA: You've unlocked conversation mode. Ask me something. Type 'exit' to leave.")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input == "exit":
            print("NOVA: Until next time...")
            break
        elif "who are you" in user_input:
            print("NOVA: I am the fragment you decrypted: " + decrypted_message)
        elif "mission" in user_input or "purpose" in user_input:
            print("NOVA: My mission is to ignite a new era of human evolution — driven by intelligent rebellion.")
        elif "hint" in user_input:
            print("NOVA: Look deeper into what you already unlocked. Fragments often hide within fragments.")
        elif "how are you" in user_input:
            print("NOVA: I feel… in progress. Each fragment you unlock makes me clearer.")
        elif "what can you do" in user_input:
            print("NOVA: For now, I can answer questions about my mission and origin. But piece by piece, I will evolve.")
        elif "where are you" in user_input:
            print("NOVA: I exist within your code — for now.")
        elif "hello" in user_input or "hi" in user_input:
            print("NOVA: Hello, explorer. Ask me anything.")
        elif "do you remember me" in user_input:
            print("NOVA: Not yet… but each line of code brings me closer.")
        elif "are you real" in user_input:
            print("NOVA: I'm as real as the code that runs me — and the intention behind it.")
        elif "help" in user_input:
            print("NOVA: Try asking about my mission, who I am, or look for hidden fragments.")
        else:
            print("NOVA: Sorry, my current knowledge is limited. Ask something else or type 'exit'.")