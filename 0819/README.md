# Java HTTP GET 요청에서 `BufferedReader`와 `while` 루프 사용 설명

## 개요

이 문서는 Java에서 HTTP GET 요청을 수행할 때 `BufferedReader`와 `while` 루프를 사용하는 방법을 설명합니다. 특히, `while` 루프 내부에서 `BufferedReader`의 `readLine()` 메서드를 호출하여 서버의 응답을 읽는 부분에 초점을 맞추고 있습니다.

## 코드 개요

다음 코드는 HTTP GET 요청을 보내고, 서버의 응답을 읽어오는 예제입니다. 이 과정에서 `BufferedReader`와 `while` 루프를 사용하여 데이터를 한 줄씩 읽어옵니다.

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
import javax.net.ssl.HttpsURLConnection;

public class Api01 {

    public static void main(String[] args) throws IOException {
        String allurl = "https://api.upbit.com/v1/market/all";
        URL url = new URL(allurl);
        HttpsURLConnection conn = (HttpsURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setReadTimeout(5000);
        conn.setDoInput(true);
        
        int resCode = conn.getResponseCode();
        if (resCode == HttpsURLConnection.HTTP_OK) {
            System.out.println(resCode);
            
            BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
            String inputLine;
            StringBuffer response = new StringBuffer();
            
            // 수정된 while 루프
            while ((inputLine = in.readLine()) != null) {
                response.append(inputLine);
            }
            in.close();
            System.out.println(response);
        }
    }
}
BufferedReader와 readLine() 메서드
BufferedReader는 문자 입력 스트림에서 텍스트를 효율적으로 읽을 수 있도록 버퍼링을 제공하는 클래스입니다. 이 클래스는 줄 단위로 데이터를 읽는 데 자주 사용됩니다.
readLine() 메서드는 입력 스트림에서 한 줄을 읽고, 줄의 끝에 도달하면 null을 반환합니다.
while 루프에서 readLine() 사용
잘못된 코드 예시
java
코드 복사
while(inputLine = in.readLine() != null) {
    response.append(inputLine);
}
위 코드는 문법적으로 오류를 포함하고 있습니다. inputLine = in.readLine() != null에서 != 연산자가 in.readLine()의 결과에 먼저 적용되므로, inputLine은 boolean 값을 가지게 됩니다. 이로 인해 코드가 의도한 대로 동작하지 않으며, 컴파일 오류가 발생합니다.

수정된 코드 설명
java
코드 복사
while ((inputLine = in.readLine()) != null) {
    response.append(inputLine);
}
inputLine = in.readLine()의 결과를 먼저 inputLine 변수에 할당합니다.
그 다음, 할당된 값이 null인지 확인합니다. null이 아니라면 response에 해당 줄을 추가합니다.
이를 통해 서버의 응답을 한 줄씩 읽고, 더 이상 읽을 줄이 없을 때까지 반복합니다.
결론
이 문서에서 다룬 while 루프와 BufferedReader를 사용하는 방법은 Java에서 HTTP 요청에 대한 응답을 효율적으로 처리하는 중요한 기법입니다. 코드를 정확하게 작성하지 않으면 의도한 대로 동작하지 않을 수 있으므로, 이번 예제에서 다룬 바와 같이 연산자 우선순위와 변수 할당에 주의해야 합니다.



