package chat;

import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

public class ChatClient {
	
	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		System.out.printf("채팅방에 입장하려면 닉네임을 입력하시오");
		
		String nm = scan.nextLine();
		
		try {
			Socket soc = new Socket("192.168.0.12", 9001);
			System.out.println("접속 성공");
			SendThread send = new SendThread(soc, nm);
			ReceiveThread recive = new ReceiveThread(soc);
			send.start();
			recive.start();
		} catch (UnknownHostException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
				
	}

}
