//package b10;
import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.*;
import java.util.Scanner;

public class Server implements Runnable {
	public static Scanner sc=new Scanner(System.in);
	public Socket sock;
	public Server(Socket s)
	{
		sock=s;
	}	
	public static void main(String[] args) throws InterruptedException 
	{
		ServerSocket ss;
		try
		{
			ss=new ServerSocket(25000);
			while(true)
			{
				System.out.println("Listening...");
				Socket server =ss.accept();
				Server Serv=new Server(server);
				(new Thread(Serv)).start();
			}		
		}catch(IOException e)
		{
			e.printStackTrace();
		}
	}

	@Override
	public void run() 
	{
		System.out.println("Connected to : "+sock.getRemoteSocketAddress());
		try
		{
			DataInputStream in=new DataInputStream(sock.getInputStream());
			long threadId=Thread.currentThread().getId();
			String Id="Current Thread Id is: "+threadId;
			Id+=" : "+in.readUTF();
			System.out.println(Id);
			
			DataOutputStream out=new DataOutputStream(sock.getOutputStream());
			out.writeUTF("Connected...\n");
			out.writeUTF("Do you want to Quit? (y/n)");
			char ch=in.readChar();
			while(ch!='y' && ch!='Y')
			{
				String temp=in.readUTF();
				System.out.println("Echoing("+threadId+"): "+temp);
				out.writeUTF(temp);
				out.writeUTF("Do you want to Quit? (y/n)");
				ch=in.readChar();
			}
			System.out.println("Thread with Id: "+threadId+" closed.");
			out.close();
			in.close();
			sock.close();
			
			
		} catch (IOException e) {
			e.printStackTrace();
		}finally
		{	
		}	
	}
}
