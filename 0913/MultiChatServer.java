package chat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;

public class MultiChatServer {

    private ArrayList<Client> clientList = new ArrayList<>();
    
    
    public static void main(String[] args) {
    	MultiChatServer server = new MultiChatServer();
    	server.serverStart();
	}

    public void serverStart()
    {
    	ServerSocket server = null;
    	
    	try {
			server = new ServerSocket(9001);
			System.out.println("9001포트 서버 오픈");
			while(true)
			{
				Socket soc = server.accept();
				System.out.println("요청 수락");
				System.out.println(soc.getRemoteSocketAddress());
				
				Client client = new Client(soc);
				client.start();
				clientList.add(client);
				
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
    }
    

    
    public class Client extends Thread {
        Socket soc;
        PrintWriter writer;
        String name;

        public Client(Socket soc) {
            this.soc = soc;
            try {
                writer = new PrintWriter(soc.getOutputStream(), true);
            } catch (IOException e) {
                e.printStackTrace();
            }
        }

        @Override
        public void run() {
            BufferedReader reader = null;
            try {
                reader = new BufferedReader(new InputStreamReader(soc.getInputStream()));
                name = reader.readLine(); 
                sendAll(name + " 님이 입장하였습니다");

                while (true) {
                	String msg = reader.readLine();
                    if (msg==null || msg.isEmpty()) {
                        break;
                    }
                    sendAll(msg);
                }
            } catch (IOException e) {
                e.printStackTrace();
            } finally {
            	sendAll(name + "님이 퇴장하셨습니다.");
            	clientList.remove(this);
                try {
                    if (soc != null) {
                        soc.close();
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    public void sendAll(String msg) {
        for (Client client : clientList) {
            client.writer.println(msg);
        }
    }

    public void addClient(Socket soc) {
        Client newClient = new Client(soc);
        clientList.add(newClient);
        newClient.start(); 
    }
}
