import java.util.ArrayList;
import java.util.List;
class Equilibrium
{
    public static void equlibrium(int A[])
    {
        int sum = 0;
        int left= 0;
        int right = 0;
        int b[]= new int[A.length];
        b[0]=0;
        for(int i =0;i<A.length;++i)
        {
            sum += A[i];
        }
        for(int i=1;i<A.length;i++)
        {
            b[i]=b[i-1]+A[i-1];
        }
        for( int i=0;i<A.length;i++)
        {
            left = b[i]-A[i];
            right = sum - b[i];
            if(left == right)
            {
                System.out.println("Equilibrium index found at" + i);
            }
        }
    }
    public static void main (String [] args)
    {
        int[] A = {1,2,0,0,1,2};
        equlibrium(A);
    }
}