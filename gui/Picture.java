import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.io.*;
import javax.imageio.*;
import java.awt.image.*;
import java.util.*;

public class Picture extends JPanel{
	BufferedImage image;
	String filename;

	public Picture(String filename){
		this.filename = filename;
       try {                
          image = ImageIO.read(new File(filename));
       } catch (IOException ex) {}
	}

	@Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.drawImage(image, 0, 0, this);           
    }
}