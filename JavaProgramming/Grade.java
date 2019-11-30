
package extracredit3;

public class Grade 
	{
    private float grade;
    private String cn;
    public Grade()
    {
        cn = "unknown";
    }
        public Grade(String x,float gp)
        {
            cn = x;
            System.out.println("Course Name is " + x);
            if (gp >= 90)
            {
                System.out.println("Your Grade is A");
            }
            else if (gp >= 80 && gp < 90)
            {
                System.out.println("Your Grade is B");
            }
            else if (gp >= 70 && gp < 80)
            {
                System.out.println("Your Grade is C");
            }
            else if (gp >=60 && gp < 70)
            {
                System.out.println("Your Grade is D");
            }
            else
                System.out.println("Your Grade is F");
        }
        public String getCN()
        {
            return cn;
        }
        public void setCourse (String cnn)
        {
            cn = cnn;
        }
        public void setGrade (float gg)
        {
            if (gg >= 0)
                grade = gg;
            else
            {
               System.err.println("Grade can't be Negative");
            }
        }
}

