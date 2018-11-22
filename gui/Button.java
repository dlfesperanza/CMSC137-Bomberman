import javax.swing.*;
import java.awt.*;
import java.io.*;
import java.util.*;
import javax.imageio.*;

class Button extends JPanel{
	private String filename;
	private Image img;
	private int xPos, yPos;

	public Button(int xPos, int yPos, String filename){
	 	this.setLayout(new BorderLayout());
	 	this.setOpaque(false);
		this.xPos = xPos;
		this.yPos = yPos;
		this.filename = filename;
		
	}
	
	@Override
	public void paintComponent(Graphics g){
		super.paintComponent(g);

		try {
			img = ImageIO.read(new File(filename));	
		} catch(Exception e) {
			System.out.println(e.getMessage());
		}

		Graphics2D g2d = (Graphics2D) g;

		g2d.drawImage(this.img, this.xPos, 0,null);
		Toolkit.getDefaultToolkit().sync();
	}
}