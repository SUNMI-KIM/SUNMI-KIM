package CharArrayStack;

public class CharArrayStack {
	int top = -1;
	  char[] elements;
	  int maxStackSize;

	  public CharArrayStack(int maxStackSize){
	    top = -1;
	    elements = new char[maxStackSize];
	  }
	  public boolean isFull() {
	    return top >= elements.length-1;
	  }
	  public CharArrayStack add(char item) {
	    if( isFull() ) {
	      throw new RuntimeException("Stack is full");
	    }
	    top++;
	    elements[top] = item;
	    return this;
	  }
	  public boolean isEmpty() {
	    return top < 0;
	  }
	  public char delete() {
	    if( isEmpty() ) {
	      throw new RuntimeException("Stack is Empty!");
	    }
	    return elements[top--];
	  }
	  public void Clear() {
	    elements = new char[elements.length];
	    top = -1;
	  }
	}



