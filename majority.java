class majority
{
    public static int majorityelement(int[]A)
    {
        System.out.print("\u000C");
        int m = -1;
        int i = 0;
        for (int j = 0;j<A.length;j++)
        {
            if(i == 0)
            {
                m =A[j];
                i=1;
            }
            else if(m==A[j])
            {
                i++;
            }
            else
            {
                i--;
            }
        }
        return m;
    }
    public static void main(String [] args)
    {
        int [] A={1,8,7,4,1,2,2,2,2,2,2};
        System.out.println("Majority element is = "+ majorityelement(A));
    }
}           