import javax.swing.*;
import java.util.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;


public class MenuPanel extends JPanel{
	JPanel panel;
	MainFrame mainframe;
	Button startBtn;
	Button howtoplayBtn;
	Button highscoreBtn;
	Button exitBtn;
	Button backBtn;
	JPanel buttonPanel;

	public MenuPanel(JPanel panel, MainFrame frame){
		this.panel = panel;
		this.mainframe = frame;

		this.setLayout(new BorderLayout());
		this.setOpaque(false);
		this.setComponents();
	}

	void setComponents(){
		this.buttonPanel = new JPanel();
		buttonPanel.setLayout(new GridLayout(5, 1));
		buttonPanel.setPreferredSize(new Dimension(500, 300));
		buttonPanel.setOpaque(false);

		this.startBtn = new Button(200,250,"./images/start-def.png");
		startBtn.addMouseListener(new MouseListener(){
			public void mouseClicked(MouseEvent e){
				Picture startPanel = new Picture("./images/start-bg.png");
				startPanel.setLayout(new GridLayout(5, 1));
				backBtn = new Button(0,20,"./images/back.png");
				backBtn.addMouseListener(new MouseListener(){
					public void mouseClicked(MouseEvent e){
						Picture bgPanel = new Picture("./images/background.png");
						bgPanel.setLayout(new CardLayout());
						MenuPanel mainmenu = new MenuPanel(panel, mainframe);
						bgPanel.add(mainmenu);
						panel.add(bgPanel,"bg");
						mainframe.setPreferredSize(new Dimension(600,505));
						mainframe.setContentPane(panel);
						mainframe.pack();
					}
					public void mousePressed(MouseEvent ke){}
					public void mouseExited(MouseEvent ke){}
					public void mouseReleased(MouseEvent e){}
					public void mouseEntered(MouseEvent e){}
				});
				startPanel.add(backBtn);
				mainframe.setPreferredSize(new Dimension(800,505));
				mainframe.setContentPane(startPanel);
				mainframe.pack();
			}
			public void mousePressed(MouseEvent ke){}
			public void mouseExited(MouseEvent ke){}
			public void mouseReleased(MouseEvent e){}
			public void mouseEntered(MouseEvent e){}
		});

		this.howtoplayBtn = new Button(190,250,"./images/howtoplay-def.png");
		howtoplayBtn.addMouseListener(new MouseListener(){
			public void mouseClicked(MouseEvent e){
				Picture howtoplayPanel = new Picture("./images/howtoplay-bg.png");
				howtoplayPanel.setLayout(new GridLayout(5, 1));
				backBtn = new Button(0,20,"./images/back.png");
				backBtn.addMouseListener(new MouseListener(){
					public void mouseClicked(MouseEvent e){
						Picture bgPanel = new Picture("./images/background.png");
						bgPanel.setLayout(new CardLayout());
						MenuPanel mainmenu = new MenuPanel(panel, mainframe);
						bgPanel.add(mainmenu);
						panel.add(bgPanel,"bg");
						mainframe.setContentPane(panel);
						mainframe.pack();

					}
					public void mousePressed(MouseEvent ke){}
					public void mouseExited(MouseEvent ke){}
					public void mouseReleased(MouseEvent e){}
					public void mouseEntered(MouseEvent e){}
				});
				howtoplayPanel.add(backBtn);
				mainframe.setContentPane(howtoplayPanel);
				mainframe.pack();
			}
			public void mousePressed(MouseEvent ke){}
			public void mouseExited(MouseEvent ke){}
			public void mouseReleased(MouseEvent e){}
			public void mouseEntered(MouseEvent e){}
		});
		this.highscoreBtn = new Button(190,250,"./images/highscore-def.png");
		highscoreBtn.addMouseListener(new MouseListener(){
			public void mouseClicked(MouseEvent e){
				Picture highscorePanel = new Picture("./images/highscore-bg.png");
				highscorePanel.setLayout(new GridLayout(5, 1));
				backBtn = new Button(0,20,"./images/back.png");
				backBtn.addMouseListener(new MouseListener(){
					public void mouseClicked(MouseEvent e){
						Picture bgPanel = new Picture("./images/background.png");
						bgPanel.setLayout(new CardLayout());
						MenuPanel mainmenu = new MenuPanel(panel, mainframe);
						bgPanel.add(mainmenu);
						panel.add(bgPanel,"bg");
						mainframe.setContentPane(panel);
						mainframe.pack();

					}
					public void mousePressed(MouseEvent ke){}
					public void mouseExited(MouseEvent ke){}
					public void mouseReleased(MouseEvent e){}
					public void mouseEntered(MouseEvent e){}
				});
				highscorePanel.add(backBtn);
				mainframe.setContentPane(highscorePanel);
				mainframe.pack();
			}
			public void mousePressed(MouseEvent ke){}
			public void mouseExited(MouseEvent ke){}
			public void mouseReleased(MouseEvent e){}
			public void mouseEntered(MouseEvent e){}
		});
		this.exitBtn = new Button(200,250,"./images/exit-def.png");
		exitBtn.addMouseListener(new MouseListener(){
			public void mouseClicked(MouseEvent e){
				mainframe.dispose();
			}
			public void mousePressed(MouseEvent ke){}
			public void mouseExited(MouseEvent ke){}
			public void mouseReleased(MouseEvent e){}
			public void mouseEntered(MouseEvent e){}
		});

		this.buttonPanel.add(startBtn);
		this.buttonPanel.add(howtoplayBtn);
		this.buttonPanel.add(highscoreBtn);
		this.buttonPanel.add(exitBtn);
		this.add(buttonPanel, BorderLayout.SOUTH);
	}
}