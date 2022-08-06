package ParenthesesChecker;

import java.util.Arrays;
import CharArrayStack.CharArrayStack;

public class ParenthesesChecker {
	 char[] open;
	 char[] close;
	 CharArrayStack stack;
	 public ParenthesesChecker(char[] open, char[] close){
	    this.open = open;
	    this.close = close;
	    stack = new CharArrayStack(100); }
	    
	 boolean isParenthese(char p) {
		    if ( isOpen(p)) return true;
		    if ( isClose(p)) return true;
		    else return false;
		  }
	 boolean isOpen(char p) {
		 	for(int i = 0; i<open.length; i++) {
		 		if(p == open[i]) {
		 			return true;
		 		}
		 	}
		 	return false;
		  }
	 boolean isClose(char p) {
		 for(int i = 0; i<close.length; i++) {
		 		if(p == close[i]) {
		 			return true;
		 		}
		 	}
		 	return false;
		  }
		  
	 boolean isMatch(char p1, char p2) {
			int i1 = -1;
			int i2 = -2;
		    if (!isOpen(p1)) return false;
		    if (!isClose(p2)) return false;
		    for(int r = 0; r<open.length; r++) {
		    	if(p1 == open[r])
		    		i1 = r;
		    }
		    for(int i = 0; i<close.length; i++) {
		    	if(p2 == close[i])
		    		i2 = i;
		    }
		    return i1 == i2;
		  }
	 boolean validate(String expression) {
		    stack.Clear();
		    for(int i = 0; i<expression.length(); i++) {
		      char test = expression.charAt(i);
		      if( !isParenthese(test) ) continue;
		      if( isOpen(test) ) {
		        stack.add(test);
		      }
		      else {
		        char last = stack.delete();
		        if(!isMatch(last, test)) return false;
		      }
		    }
		    return stack.isEmpty();
		  }
	public static void main(String[] args) {
		
		char[] open = {'(', '{', '<', '['};
	    char[] close = {')', '}', '>', ']'};
	    ParenthesesChecker  n1 = new ParenthesesChecker(open, close);
	    System.out.println("(1+2)" + ":=" + n1.validate("(1+2)"));
	    System.out.println("2+(2+[3+<4*5>]-9)/2" + ":=" + n1.validate("2+(2+[3+<4*5>]-9)/2"));
	    System.out.println("(3+(3+(4+5]))" + ":=" + n1.validate("(3+(3+(4+5]))"));
	    System.out.println("(4*[1+(3-5]))" + ":=" + n1.validate("(4*[1+(3-5]))"));
	    System.out.println("5+(5+6*7+(9+[2/5])" + ":=" + n1.validate("5+(5+6*7+(9+[2/5])"));
	}

}
