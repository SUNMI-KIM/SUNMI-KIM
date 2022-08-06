package BST;

import java.util.Arrays;
public class BST {
	int data;
	BST llink;
	BST rlink;
	int n = 0;
	BST root;
	int[] arr = new int[100];
	int i = 0;
	public BST() {
		root = new BST(null, 0, null);
	}
	
	public BST(BST L, int data, BST R) {
		this.data = data;
		this.llink = L;
		this.rlink = R;
	}
	
	void inorder() {
		inorder(root);
	}
	
	void postorder(){	
		postorder(root);
	}
	
	void preorder() {
		preorder(root);
	}
	
	void inorder(BST p) {
		if(p != null) {
			inorder(p.llink);
			System.out.print(p.data + " ");
			inorder(p.rlink);
		}
	}
	
	void postorder(BST p) {
		if(p != null) {
			postorder(p.llink);
			postorder(p.rlink);
			System.out.print(p.data + " ");
		}
	}
	void preorder(BST p) {
		if(p != null) {
			System.out.print(p.data + " ");
			preorder(p.llink);
			preorder(p.rlink);
		}
	}
	
	void Add(int element) {
		BST Element = new BST(null, element, null);
		if (n == 0) {
			n++;
			root.data = element;
			root.llink = null;
			root.rlink = null;
			arr[0] = root.data;
			i++;
		}
		else if(n > 0) {
			BST indata = root;
			n++;
			while(true) {
				if(indata.data > element) {
					if(indata.llink == null) {
						indata.llink = Element;
						arr[i] = Element.data;
						i++;
						break;
					}
					else {
						indata = indata.llink;
					}
				}
				else if(indata.data < element) {
					if(indata.rlink == null) {
						indata.rlink = Element;
						arr[i] = Element.data;
						i++;
						break;
					}
					else {
						indata = indata.rlink;
					}
				}
			}
		}
	}
	
	int getTreeHeight() {
		if (n%2 == 0) {
			return n/2;
		}
		else {
			return (n-1)/2;
		}
	}
	int[] higher(int element) {
		int[] returnarr = new int[i];
		int l = 0;
		for(int r = 0; r<i+1; r++) {
			if(arr[r] > element) {
				returnarr[l] = arr[r];
				l++;
			}
		}
		int[] ra = Arrays.copyOf(returnarr, l);
		return ra;
	}
	
	public static void main(String[] args) {
		BST bst = new BST();
		bst.Add(23);
		bst.Add(39);
		bst.Add(7);
		bst.Add(20);
		bst.Add(14);
		bst.Add(15);
		bst.Add(46);
		bst.Add(66);
		bst.Add(75);
		bst.Add(49);
		bst.Add(32);
		bst.inorder();
		System.out.println();
		bst.preorder();
		System.out.println();
		bst.postorder();
		System.out.println();
		System.out.println(bst.getTreeHeight());
		System.out.println(Arrays.toString(bst.higher(40)));
	}
}