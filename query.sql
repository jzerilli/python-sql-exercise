CREATE TABLE IF NOT EXISTS stats(
    rk INT NOT NULL, 
    player VARCHAR (50) NOT NULL, 
    team VARCHAR (50) NOT NULL, 
    player_id INT NOT NULL PRIMARY KEY, 
    pos VARCHAR (3) NOT NULL,  
    g INT NOT NULL, 
    ab INT NOT NULL, 
    r INT NOT NULL, 
    h INT NOT NULL, 
    double INT NOT NULL,
    triple INT NOT NULL,
    hr INT NOT NULL, 
    rbi INT NOT NULL, 
    bb INT NOT NULL, 
    so INT NOT NULL, 
    sb INT NOT NULL, 
    cs INT NOT NULL, 
    ba FLOAT NOT NULL, 
    obp FLOAT NOT NULL, 
    slg FLOAT NOT NULL, 
    ops FLOAT NOT NULL, 
    ibb INT NOT NULL, 
    hbp INT NOT NULL, 
    sac INT NOT NULL, 
    sf INT NOT NULL, 
    tb INT NOT NULL, 
    xbh INT NOT NULL, 
    gdp INT NOT NULL, 
    goo INT NOT NULL, 
    ao INT NOT NULL, 
    go_ao FLOAT NOT NULL, 
    np INT NOT NULL, 
    pa INT NOT NULL
);

SELECT player, (0.689*(bb - ibb) + 0.722*hbp + 0.892*(h - double - triple - hr) + 1.283*double + 1.635*triple + 2.135*hr) 
    / (ab + bb - ibb + sf + hbp) AS wOBA
from stats
order by 2 desc;



