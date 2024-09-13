package chat;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.Socket;

public class ReceiveThread extends Thread {

    private Socket soc;

    public ReceiveThread(Socket soc) {
        this.soc = soc;
    }

    public void run() {
        BufferedReader reader = null;
        try {
            reader = new BufferedReader(new InputStreamReader(soc.getInputStream(), "UTF-8"));

            while (true) {
                String msg = reader.readLine();
                if (msg == null || msg.equals("")) {
                    break;
                }
                System.out.println(msg);
            }
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                if (soc != null) {
                    soc.close();
                }
                if (reader != null) {
                    reader.close();  
                }
            } catch (IOException e) {
                e.printStackTrace();  
            }
        }
    }
}
