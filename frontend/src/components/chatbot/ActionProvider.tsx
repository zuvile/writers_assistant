import { fetchChatResponse } from "../../api";

class ActionProvider {
  createChatBotMessage: any;
  setState: any;

  constructor(createChatBotMessage: any, setStateFunc: any) {
    this.createChatBotMessage = createChatBotMessage;
    this.setState = setStateFunc;
  }

  greet() {
    const greetingMessage = this.createChatBotMessage(
      "I am your beta reader. I am here to help you with your writing. How can I help you today?",
    );
    this.updateChatbotState(greetingMessage);
  }

  async chat(message: string) {
    try {
      const response = await fetchChatResponse(message);
      if (message) {
        const responseMessage = this.createChatBotMessage(response);
        this.updateChatbotState(responseMessage);
      }
    } catch (error) {
      console.error("Error in fetchChatResponse:", error);
    }
  }

  updateChatbotState(message: any) {
    this.setState((prevState: any) => ({
      ...prevState,
      messages: [...prevState.messages, message],
    }));
  }
}

export default ActionProvider;
