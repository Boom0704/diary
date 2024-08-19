package api;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import javax.net.ssl.*;

public class Api01 {

	public static void main(String[] args) throws IOException {
		// TODO Auto-generated method stub
		String allurl = "https://api.upbit.com/v1/market/all";
		URL url = new URL(allurl);
		HttpsURLConnection conn =(HttpsURLConnection) url.openConnection();
		conn.setRequestMethod("GET");
		conn.setReadTimeout(5000);
		conn.setDoInput(true);
		int resCode = conn.getResponseCode();
		if(resCode == HttpsURLConnection.HTTP_OK) {
			System.out.println(resCode);
			
			BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
			String inputLine;
			StringBuffer response = new StringBuffer();
			while ((inputLine = in.readLine()) != null) {
			    response.append(inputLine);
			}

			in.close();
			System.out.println(response);
		}
	}

}
