package RamdomintArray;
import java.util.Random;


public class RamdomintArray {
	static void accumulatedSum(int[] a) {
		int[] sum = new int[a.length];
		for(int i = 0; i<a.length; i++) {
			int b = 0;
			for(int r = 0; r<i+1; r++) {
				b += a[r];
			}
			sum[i] = b;
			System.out.println("sum["+ i + "] = " + sum[i]);
		}
	}
	public static void main(String[] args) {
		Random rand = new Random();
		int[] value = new int[5];
		for(int i = 0; i< value.length; i++) {
			value[i] = rand.nextInt( 5 + i );
		}
		accumulatedSum(value);
		
	}

}
