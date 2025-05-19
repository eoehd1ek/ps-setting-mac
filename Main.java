import java.io.*;
import java.math.BigInteger;
import java.util.*;

// 백준 자바 제출 파일의 클래스명은 항상 Main
public class Main {

    public static void main(String[] args) throws IOException {
        // 백준 제출 시 다음 2줄 코드 삭제하기.
        // input.txt에서 입력받고, output.txt에 출력하도록 설정하는 코드.
        System.setIn(new FileInputStream("input.txt"));
        System.setOut(new PrintStream(new FileOutputStream("output.txt")));

        // 빠른 입출력을 위한 BufferedReader, BufferedWriter.
        // 많은 데이터의 입력, 또는 출력 문제가 아닌 경우 사용하지 않아도 괜찮음.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        // input EX: 1 2
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int result = a + b;
        bw.write(result + "\n");

        // 문자열 입력 및 숫자 출력 방법
        // str.length() -> int 타입, bw.write 매개변수는 문자열을 받음. type miss match
        // 따라서 숫자 + 문자열 연산을 하면 문자열로 형변환된다.
        // ex: 1 + "\n"
        String str = br.readLine();
        bw.write(str.length() + "\n");

        // bw.close() 호출에 bw.flush()가 포함되어 있음.
        // flush() 미호출시 콘솔에 bw.write(result + "\n"); 결과가 출력되지 않음. => 틀렸습니다.
        br.close();
        bw.close();
    }
}
