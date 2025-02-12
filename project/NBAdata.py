from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

gamefinder = leaguegamefinder.LeagueGameFinder()
games = gamefinder.get_data_frames()[0]

# Show the first few rows
print(games.head())


"""_Statinfo_
SEASON LEADERS
    Points per game
    Rebounds per game
    Assists per game
    Blocks per game
    steals per game
    fg % per game
    3 pointers made (total)
    3 point % (total)
    Free Throw Percentage

ADVANCED
    NET rating
    OFFENSIVE RATING
    DEFENSIVE RATING

MISCELLANEOUS
    Fast break points per game
    2nd chance points per game
    points in the paint per game

PLAYER TRACKING SPEED
    Pace
    Miles per game
    avg speed

HUSTLE
    Deflections per game
    loose balls rec per game
    screen assists per game

SCORING
    % of points 3-pointers
    % of points in the paint
    % of points mid-range

RESEARCH
    *effective field goal percentage (eFG%)
    *offensive rebounding percentage (OREB%)
    *turnover ratio (TO ratio) Assist/Turnover Ratio
    *free throw attempt rate (FTA rate)
*Dean Oliver Team Four Factor Rating = *((0.4*eFG%)-(0.25*TOV)+(0.2*OREB)+(0.15*FTR))
*Dean Oliver Opponent Four Factor Rating = ((0.4*OppeFG%)-(0.25*OppTOV)+(0.2*OppOREB)+(0.15*OppFTR))
**Dean Oliver Net Four Factor Rating = DO Team FF Rating – DO Opp FF Rating
    FT %
    Rebound Differential
    3pt %
    FG %
NBA PIE rating (Player Impact Estimate)
    +/- 
Sully's Net Four Factor Rating
    Sully’s Team Four Factor Rating = *((0.50*eFG%)-(0.30*TOV)+(0.15*OREB)+(0.05*FTR))*Sully’s 
    Opponent Four Factor Rating = ((0.50*OppeFG%)-(0.30*OppTOV)+(0.15*OppOREB)+(0.05*OppFTR))
    Sully’s Net Four Factor Rating = Sully Team FF Rating – Sully Opp FF Rating



https://www.watchstadium.com/posts/which-nba-statistics-actually-translate-to-wins-07-13-2019
https://www.basketball-reference.com/about/factors.html
https://www.reddit.com/r/nba/comments/g4w5bp/the_nbas_most_valuable_statistic_award_goes_to/

"""