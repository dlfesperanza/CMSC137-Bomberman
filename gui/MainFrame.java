import javax.swing.*;
import java.util.*;
import java.awt.*;
import java.net.*;

public class MainFrame extends JFrame{
	MenuPanel menuPanel;
	JPanel panel;

	public MainFrame(String name){
		super(name);	
		this.setPreferredSize(new Dimension(600,505));
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setResizable(false);

		this.panel = new JPanel();
		panel.setLayout(new CardLayout());

		this.menuPanel = new MenuPanel(this.panel, this);

		Picture bgPanel = new Picture("./images/background.png");
		bgPanel.setLayout(new CardLayout());

		// JPanel bg = new JPanel();
		// bg.setLayout(new CardLayout());
		// URL url = MainFrame.class.getResource("./images/background.gif");
		// Icon icon = new ImageIcon(url);
		// JLabel bgIcon = new JLabel(icon);
		// bgIcon.setBounds(0,0,500,700);
		// bg.add(menuPanel);
		// bg.add(bgIcon);

		bgPanel.add(menuPanel);
		panel.add(bgPanel, "background");


		this.setContentPane(panel);

		this.pack();
		this.setVisible(true);
	}
}