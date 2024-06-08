import "react-chatbot-kit/build/main.css";
import React from "react";
import Chatbot from "react-chatbot-kit";
import config from "./configs/chatbotConfig";
import MessageParser from "./chatbot/MessageParser";
import ActionProvider from "./chatbot/ActionProvider";

const ChatbotComponent = () => {
  return (
    <div className="container overflow-auto">
      <Chatbot
        config={config}
        messageParser={MessageParser}
        actionProvider={ActionProvider}
      />
    </div>
  );
};

export default ChatbotComponent;
