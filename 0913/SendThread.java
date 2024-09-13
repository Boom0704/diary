package chat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class SendThread extends Thread {
	
	private Socket soc;
	
	private String name;

	public SendThread(Socket soc, String name) {
		this.soc = soc;
		this.name = name;
	}
	
	public void run()
	{
		BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
		
		try {
			PrintWriter writer = new PrintWriter(soc.getOutputStream());
			
			writer.println(name);
			writer.flush();
			while(true)
			{
				System.out.printf("입력: ");
				String msg = reader.readLine();
				if(msg == null || msg.equals(""))
						break;
				writer.println(name + " : " + msg);
				writer.flush();
			}
			
		} catch (IOException e) {
			e.printStackTrace();
		}
		finally 
		{
			try {
				if (soc != null) soc.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		
	}
	
}
