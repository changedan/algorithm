package baekjoon.number_theory;

import java.util.Scanner;

public class B1037 {
	public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int num = sc.nextInt();
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for (int i = 0; i < num; i++) {
            int temp = sc.nextInt();
            if (temp > max) {
                max = temp;
            }
            if (temp < min) {
                min = temp;
            }
        }
        int n = min * max;
        System.out.println(n);
        
        sc.close();
	}
	
}
