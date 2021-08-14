import threading
import keyboard
from GameControl import *
import os
import pyautogui
from ThreadGame import *
from Util import *

#coordinate
CLAIM_REWARD=(566, 541)
CHANGE_SHIKI_COORDINATE=(468,374)
SLIDE_STORY_COORDINATE=[(200,200),(1000,200)]
SHIKI_LEVEL_COORDINATE=(52,580)
SLIDE_CHANGE_SHIKI=[(600, 500),(870, 500)]
REGION_FIND_FULL_EXP_LEADER=[(0,0),((300,600))]
REGION_CHANGE_FULL_EXP_LEADER=[(600,0),((1100,300))]
REGION_CHANGE_FULL_EXP_PASENGER=[(0, 0),(1108, 402)]
REGION_FIND_FULL_EXP_SOLO=[(0,0),(520, 600)]
REGION_CHANGE_EXP_SOLO=[(387, 61),(1105, 374)]
CHANGE_FOOD_RIGHT_COORDINATE=(938, 301)
CHANGE_FOOD_MIDDLE_COORDINATE=(553, 300)
CHANGE_FOOD_LEFT_COORDINATE=(157, 288)
CHANGE_FOOD_LEADER_RIGHT_COORDINATE=(826, 261)
REFRESH_SEAL_COORDINATE=(438, 551)
CHOOSE_LEVEL_HARD_COORDINATE=(409, 195)
CHOOSE_FRIEND_COORDINATE=(452, 95)
SLIDE_FRIENDLIST=[(493, 246),(525, 436)]
INVITE_MEMBER_COORDINATE=(681, 504)
TEAM_COORDINATE=(569, 492)
STORY_BACK_COORDINATE=(35, 51)
STORY_OK_COORDINATE=(681, 351)
OK_SOUL_DIALOG_COORDINATE=(679, 375)
CHECKBOX_COORDINATE=(390, 300)
SOUL_ICON_COORDINATE=(173, 584)
INVITE_SOUL_ONLY_COORDINATE=(670, 445)
SLIDE_LEVEL_OROCHI=[(276, 137),(271, 505)]
CREATE_TEAM_SOUL_COORDINATE=(868, 564)
REGION_TEAM_INVITE_SOUL=[(0,0),(729, 409)]
START_SOUL_COORDINATE=(1075, 565)
INVITE_MEMBER_SOUL_COORDINATE=(681, 506)
SLIDE_FRIEND_LIST_SOUL=[(428, 169),(431, 440)]

#path
IMAGE_FAILED_PATH="./screenshots/failed.png"
IMAGE_SCREENSHOT_PATH="./screenshots/screenshot.png"
IMAGE_CONNECTING_PATH="./screenshots/connecting.png"
IMAGE_ASSISTANCE_PATH="./screenshots/accept_wantedquest.png"
IMAGE_ASSISTANCE_2_PATH="./screenshots/close.png"
IMAGE_ACCEPT_PATH="./screenshots/accept.png"
IMAGE_ACCEPT_PATH_WANTED_QUEST="./screenshots/accept_wantedquest.png"
IMAGE_OCCUPIED_PATH="./screenshots/occupied.png"
IMAGE_FOOD_INSUFFICIENCY_PATH="./screenshots/food.png"
IMAGE_CLOSE_DIALOG_PATH="./screenshots/close.png"
IMAGE_DISCONNECTED_PATH="./screenshots/disconnected.png"

IMAGE_SOUL_INVITE_PATH="./screenshots/Soul/teamInvite.png"
IMAGE_SOUL_START_PATH="./screenshots/Soul/start.png"
IMAGE_SOUL_FINISHED1_PATH="./screenshots/Soul/finished1.png"
IMAGE_SOUL_FINISHED2_PATH="./screenshots/Soul/finished2.png"
IMAGE_SOUL_INVITE_DIALOG_PATH="./screenshots/Soul/inviteDialog.png"
IMAGE_SOUL_INVITE_CHECKBOX_PATH="./screenshots/Soul/invitecheckbox.png"
IMAGE_SOUL_INVITE_CONFIRM_PATH="./screenshots/Soul/inviteconfirm.png"
IMAGE_SOUL_SUSI_PATH="./screenshots/Soul/susi.png"
IMAGE_SOUL_ICON_PATH="./screenshots/Soul/soul.png"
IMAGE_SOUL_OROCHI_PATH="./screenshots/Soul/orochi.png"
IMAGE_SOUL_OROCHI_STAGE10_PATH="./screenshots/Soul/stage10.png"
IMAGE_SOUL_TEAM_PATH="./screenshots/Soul/team.png"
IMAGE_SOUL_STAGE10_DIALOG_PATH="./screenshots/Soul/stage10TeamDialog.png"
IMAGE_SOUL_CREATE_TEAM_PATH="./screenshots/Soul/createTeam.png"
IMAGE_SOUL_CREATE_ROOM_PATH="./screenshots/Soul/createRoom.png"
IMAGE_SOUL_STAGE10_FOCUS_PATH="./screenshots/Soul/stage10Focus.png"
IMAGE_SOUL_INROOM_PATH="./screenshots/Soul/inroom.png"
IMAGE_SOUL_STAT_PATH="./screenshots/Soul/stat.png"
IMAGE_SOUL_SET_PATH="./screenshots/Soul/set.png"
IMAGE_SOUL_CLOCL_PATH="./screenshots/Soul/clock.png"




IMAGE_STORY_LAST_CHAPTER="./screenshots/Story/lastchapter.png"
IMAGE_STORY_INVITE_PATH="./screenshots/Story/invite.png"
IMAGE_STORY_INVITATION_CONFIRMED_PATH="./screenshots/Story/invitationConfirmed.png"
IMAGE_STORY_START_PATH="./screenshots/Story/start.png"
IMAGE_STORY_FIGHT_PATH="./screenshots/Story/fight.png"
IMAGE_STORY_FIGHT_BOSS_PATH="./screenshots/Story/fightBoss.png"
IMAGE_STORY_FINISHED1_PATH="./screenshots/Story/finished1.png"
IMAGE_STORY_FINISHED2_PATH="./screenshots/Story/finished2.png"
IMAGE_STORY_ACCEPT_PATH="./screenshots/Story/accept.png"
IMAGE_STORY_BACK_PATH="./screenshots/Story/back.png"
IMAGE_STORY_GET_REWARD_PATH="./screenshots/Story/getReward.png"
IMAGE_STORY_REWARD_CONFIRMED_PATH="./screenshots/Story/rewardConfirmed.png"
IMAGE_STORY_READY_PATH="./screenshots/Story/ready.png"
IMAGE_STORY_READY_MARK_PATH="./screenshots/Story/readyMark.png"
IMAGE_STORY_SELECT_LEVEL_PATH="./screenshots/Story/selectLevel.png"
IMAGE_STORY_FULL1_PATH="./screenshots/Story/full1.png"
IMAGE_STORY_FULL2_PATH="./screenshots/Story/full2.png"
IMAGE_STORY_FOOD_PATH="./screenshots/Story/food.png"
IMAGE_STORY_CHERRY_CAKE_PATH="./screenshots/Story/cherryCake.png"
IMAGE_STORY_SHIKIGAMI_SELECTED_PATH="./screenshots/Story/shikigamiSelected.png"
IMAGE_STORY_SHIKIGAMI_SELECTED1_PATH="./screenshots/Story/shikigamiSelected1.png"
IMAGE_STORY_SHIKIGAMI_SELECTED3_PATH="./screenshots/Story/shikigamiSelected3.png"
IMAGE_STORY_SHIKIGAMI_SELECTED2_PATH="./screenshots/Story/shikigamiSelected2.png"
IMAGE_STORY_SHIKIGAMI_SELECTED8_PATH="./screenshots/Story/shikigamiSelected8.png"
IMAGE_STORY_SELECTED_LEVEL_PATH="./screenshots/Story/selectedLevel.png"
IMAGE_STORY_TEAM_PATH="./screenshots/Story/team.png"
IMAGE_STORY_TEAMMATE_PATH="./screenshots/Story/teammate.png"
IMAGE_STORY_APPROVE_PATH="./screenshots/Story/approve.png"
IMAGE_STORY_SEAL_TICKET_PATH="./screenshots/Story/sealticket.png"
IMAGE_STORY_LIST_CHAPTER_PATH="./screenshots/Story/listchapter.png"
IMAGE_STORY_SPIRIT_PATH="./screenshots/Story/spirit.png"
IMAGE_STORY_ISINTEAM_PATH="./screenshots/Story/lead.png"
IMAGE_STORY_CREATE_PATH="./screenshots/Story/create.png"


IMAGE_SOUL_X_START_PATH="./screenshots/SoulX/start.png"
IMAGE_SOUL_X_FINISHED1_PATH="./screenshots/SoulX/finished1.png"
IMAGE_SOUL_X_FINISHED2_PATH="./screenshots/SoulX/finished2.png"

IMAGE_SOUL_SOUGENBI_CHALLENGE="./screenshots/Soul/sougenbiChallenge.png"

IMAGE_REALM_START_PATH="./screenshots/RealmRaid/start.png"
IMAGE_REALM_SECTION_PATH="./screenshots/RealmRaid/section.png"
IMAGE_REALM_RANK_PATH="./screenshots/RealmRaid/rank.png"
IMAGE_REALM_FINISHED1_PATH="./screenshots/RealmRaid/finished1.png"
IMAGE_REALM_FINISHED2_PATH="./screenshots/RealmRaid/finished2.png"
IMAGE_REALM_SHIKIGAMI_SELECTED_PATH="./screenshots/RealmRaid/shikigamiSelected.png"
IMAGE_REALM_SELECTION_MARK_PATH="./screenshots/RealmRaid/selectionMark.png"
IMAGE_REALM_FAILED_PATH="./screenshots/RealmRaid/failed.png"
IMAGE_REALM_RAID_PATH="./screenshots/RealmRaid/realmRaid.png"
IMAGE_REALM_PROFILE_PATH="./screenshots/RealmRaid/profile.png"
IMAGE_REALM_PRESET_PATH="./screenshots/RealmRaid/preset.png"
IMAGE_REALM_REFRESH_PATH="./screenshots/RealmRaid/refresh.png"
IMAGE_REALM_LOCK_PATH="./screenshots/RealmRaid/lock.png"
IMAGE_REALM_EMPTY_TICKET="./screenshots/RealmRaid/empty.png"

IMAGE_SEAL_TEAM_PATH="./screenshots/Seal/team.png"
IMAGE_SEAL_SEAL_PATH="./screenshots/Seal/seal.png"
IMAGE_SEAL_MATCH_PATH="./screenshots/Seal/match.png"
IMAGE_SEAL_START_PATH="./screenshots/Seal/start.png"
IMAGE_SEAL_READY_PATH="./screenshots/Seal/ready.png"
IMAGE_SEAL_FINISHED1_PATH="./screenshots/Seal/finished1.png"
IMAGE_SEAL_FINISHED2_PATH="./screenshots/Seal/finished2.png"
IMAGE_SEAL_ALL_PATH="./screenshots/Seal/all.png"
IMAGE_SEAL_JOIN_PATH="./screenshots/Seal/join.png"
IMAGE_SEAL_REFRESH_PATH="./screenshots/Seal/refresh.png"
IMAGE_SEAL_WAIT_PATH="./screenshots/Seal/wait.png"
IMAGE_SEAL_MATCH_PATH="./screenshots/Seal/match.png"

IMAGE_COOP_SEAL="./screenshots/coopwanted.png"
IMAGE_START_FIGHT="./screenshots/Event/fight.png"
IMAGE_TARGET_SHIKIGAMI="./screenshots/Event/target.png"
IMAGE_SOUL_SEDUCTRESS = "./screenshots/Event/seductress.png"
IMAGE_SOUL_GHOSTLY = "./screenshots/Event/ghostly.png"

_localVariable=threading.local()
_DETECTION_INTERVAL=0.2
_accountCount=0
_fullShikigamiCount=0
_isPaused=False
_isFullTeam=False

_detectExitThread=threading.Thread()
_accountLocker=threading.Lock()
_replaceShikigamiIfFull=True

#
class Processing(threading.Thread):
    def __init__(self,windowName,gameMode,total,isCaptain=False,isMainDMG=True):
        threading.Thread.__init__(self)
        global _accountCount
        global _detectExitThread
        global _accountLocker
        self.__isFinishRound = False
        self.__hwnd=win32gui.FindWindow(0, windowName)
        self.__gameMode=gameMode
        self.__total=total
        self.__isCaptain=isCaptain
        self.__isMainDMG=isMainDMG
        self.__id=_accountCount
        self.__gui=GameControl(self.__hwnd,0)
        self.__thread=ThreadGame()
        self.__delay=0.5
        self.__debug=False
        _accountCount+=1
        _accountLocker.acquire()
        if not _detectExitThread.is_alive():
            _detectExitThread=threading.Thread(None,self.detectPause)
            _detectAssistantThread=threading.Thread(None,self.detectAssistance)
            _detectExitThread.setDaemon(True)
            _detectAssistantThread.setDaemon(True)
            _detectExitThread.start()
            _detectAssistantThread.start()
            # _detectTargetThread=threading.Thread(None,self.targetShikigami)
            # _detectTargetThread.setDaemon(True)
            # _detectTargetThread.start()
            if self.__debug==True:
                _debugTread=threading.Thread(None,self.__gui.debug())
                _debugTread.setDaemon(True)
                _debugTread.start()
        _accountLocker.release()
#
    @property
    def accountCount(self):
        return _accountCount
#
    def gameModeSoul(self):
        printWithTime("Message: Account %s: Multiplayer Soul/Evolution"%(str(self.__id)))
        while True:
            position=self.__gui.find_game_img(IMAGE_REALM_PROFILE_PATH,thread=0.85)
            if position != False or self.__gui.find_game_img(IMAGE_SOUL_SET_PATH,thread=0.8) != False:
                printWithTime("Message: Account %s: In battle detected, sleep 5s ..."%(str(self.__id)))
                time.sleep(5)
                continue

            #whether is in room..
            if self.__gui.find_game_img(IMAGE_SOUL_INROOM_PATH,thread=0.8) != False: #and self.__gui.find_game_img(IMAGE_SOUL_CLOCL_PATH,thread=0.8) ==False:
                _localVariable.isInRoom = True
                _localVariable.isInBattle=False
            #Whether is a leader
            if self.__isCaptain:
                time.sleep(1)
                #starting..
                position=self.__gui.find_game_img(IMAGE_SOUL_START_PATH,thread=0.98,gray=0)
                if position != False:
                    printWithTime("Message: Account %s: Starting... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)
                    _localVariable.isInBattle=True
                    _localVariable.isInRoom=True
                    continue

                #invite  to continues..
                position=self.__gui.find_game_img(IMAGE_SOUL_INVITE_DIALOG_PATH,thread=0.7)
                if position != False:
                    printWithTime("Message: Account %s: Invite member to continue... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(CHECKBOX_COORDINATE)
                    time.sleep(2)
                    self.__gui.mouse_click_bg(OK_SOUL_DIALOG_COORDINATE)
                    _localVariable.isInBattle=False
                    continue

                if _isFullTeam:
                    position=self.__gui.find_game_img(IMAGE_SOUL_INVITE_PATH)
                    if position == False:
                        position=self.__gui.find_game_img(IMAGE_SOUL_START_PATH)
                        if position != False:
                            printWithTime("Message: Account %s: Full slot detectection =>> Starting game...%s: "%(str(self.__id),IMAGE_SOUL_START_PATH))
                            self.__gui.mouse_click_bg(position)
                            continue
                else:
                    if self.__gui.find_game_img(IMAGE_SOUL_INROOM_PATH,thread=0.8) != False:
                        position=self.__gui.find_game_img(IMAGE_SOUL_INVITE_PATH,1,REGION_TEAM_INVITE_SOUL[0],REGION_TEAM_INVITE_SOUL[1],thread=0.7)
                        if position != False:
                            while True:
                                position=self.__gui.find_game_img(IMAGE_SOUL_INVITE_PATH,1,REGION_TEAM_INVITE_SOUL[0],REGION_TEAM_INVITE_SOUL[1],thread=0.7)
                                if position==False:
                                    break
                                else:
                                    self.__gui.mouse_click_bg(position)
                                    time.sleep(2)
                                    position=self.__gui.find_game_img(IMAGE_STORY_INVITATION_CONFIRMED_PATH)
                                    if position != False:
                                        printWithTime("Message: Account %s: Choosing teammate..... "%(str(self.__id)))
                                        position=self.__gui.find_game_img(IMAGE_STORY_TEAMMATE_PATH)
                                        if position != False:
                                            self.__gui.mouse_click_bg(position)
                                            time.sleep(1)
                                            self.__gui.mouse_click_bg(INVITE_MEMBER_SOUL_COORDINATE)
                                            time.sleep(1)
                                            self.__gui.mouse_click_bg(START_SOUL_COORDINATE)
                                            _localVariable.isInBattle=True
                                            _localVariable.isInRoom=True
                                            printWithTime("Message: Account %s: Invite teamate..... "%(str(self.__id)))
                                            time.sleep(2)
                                        else:
                                            count=6
                                            while count>0:
                                                count-=1
                                                printWithTime("Message: Account %s: Can't finding ig, re trying..... "%(str(self.__id)))
                                                position=self.__gui.find_game_img(IMAGE_STORY_TEAMMATE_PATH)
                                                if position != False:
                                                    self.__gui.mouse_click_bg(position)
                                                    time.sleep(1)
                                                    self.__gui.mouse_click_bg(INVITE_MEMBER_SOUL_COORDINATE)
                                                    time.sleep(1)
                                                    self.__gui.mouse_click_bg(START_SOUL_COORDINATE)
                                                    _localVariable.isInBattle=True
                                                    _localVariable.isInRoom=True
                                                    printWithTime("Message: Account %s: Sucessfully finding teammate, starting battle..... "%(str(self.__id)))
                                                    break
                                                if count>3:
                                                    self.__gui.mouse_drag_bg(SLIDE_FRIEND_LIST_SOUL[0],SLIDE_FRIEND_LIST_SOUL[1])
                                                else:
                                                    self.__gui.mouse_drag_bg(SLIDE_FRIEND_LIST_SOUL[1],SLIDE_FRIEND_LIST_SOUL[0])
                        elif position ==False and _localVariable.isInBattle==False:
                            self.__gui.mouse_click_bg(START_SOUL_COORDINATE)
                            _localVariable.isInBattle=True
                            _localVariable.isInRoom=True

                #whether is outside soul room...
                # while self.__gui.find_game_img(IMAGE_SOUL_INROOM_PATH,thread=0.8) == False and _localVariable.isInBattle==False:
                #     if self.__gui.find_game_img(IMAGE_SOUL_INROOM_PATH,thread=0.8) != False or _localVariable.isInBattle==True:
                #         _localVariable.isInRoom = True
                #         break

                #     printWithTime("Message: Account %s: Not in soul room was detected, create a room... "%(str(self.__id)))
                #     #click soul icon
                #     position=self.__gui.find_game_img(IMAGE_SOUL_ICON_PATH)
                #     if position != False:
                #         self.__gui.mouse_click_bg(position)
                #         printWithTime("Message: Account %s: Clicking soul icon... "%(str(self.__id)))
                #         time.sleep(1)
                #         continue


                #     #click orochi
                #     position=self.__gui.find_game_img(IMAGE_SOUL_OROCHI_PATH)
                #     if position != False:
                #         self.__gui.mouse_click_bg(position)
                #         printWithTime("Message: Account %s: Choosing orochi... "%(str(self.__id)))
                #         time.sleep(1)
                #         continue


                #     #choose level
                #     position=self.__gui.find_game_img(IMAGE_SOUL_OROCHI_STAGE10_PATH,gray=1, thread=0.9)
                #     if position != False:
                #         printWithTime("Message: Account %s: Choosing orochi stage 10... "%(str(self.__id)))
                #         self.__gui.mouse_click_bg(position)
                #     else:
                #         printWithTime("Message: Account %s: Cant find orochi level 10, try again... "%(str(self.__id)))
                #         count=4
                #         while count>0:
                #             position=self.__gui.find_game_img(IMAGE_SOUL_OROCHI_STAGE10_PATH)
                #             if position != False:
                #                 self.__gui.mouse_click_bg(position)
                #                 time.sleep(1)
                #                 self.__gui.mouse_click_bg(CREATE_TEAM_SOUL_COORDINATE)
                #                 printWithTime("Message: Account %s: Choosing orochi stage 10... "%(str(self.__id)))
                #                 break
                #             self.__gui.mouse_drag_bg(SLIDE_LEVEL_OROCHI[1],SLIDE_LEVEL_OROCHI[0])
                #             time.sleep(1)
                #             count-=1

                #     position=self.__gui.find_game_img(IMAGE_SOUL_TEAM_PATH,thread=0.7)
                #     if position != False:
                #         self.__gui.mouse_click_bg(position)
                #         continue


                #     position=self.__gui.find_game_img(IMAGE_SOUL_CREATE_TEAM_PATH)
                #     if position != False:
                #         printWithTime("Message: Account %s: Create team... "%(str(self.__id)))
                #         self.__gui.mouse_click_bg(position)
                #         time.sleep(1)
                #         continue

                #     position=self.__gui.find_game_img(IMAGE_SOUL_CREATE_ROOM_PATH)
                #     if position != False:
                #         printWithTime("Message: Account %s: Create soul room... "%(str(self.__id)))
                #         self.__gui.mouse_click_bg(INVITE_SOUL_ONLY_COORDINATE)
                #         time.sleep(1)
                #         self.__gui.mouse_click_bg(position)
                #         _localVariable.isInRoom=True
                #         time.sleep(1)
            else:
                if self.__isMainDMG:
                    position=self.__gui.find_game_img(IMAGE_SOUL_SOUGENBI_CHALLENGE)
                    if position != False:
                        message="Message: Account %s: Start new round..."%(str(self.__id))
                        printWithTime(message)
                        self.__gui.mouse_click_bg(position)
                        continue

                else:
                    position=self.__gui.find_game_img(IMAGE_STORY_ACCEPT_PATH)
                    if position != False:
                        message="Message: Account %s: Tried to accept a new round..."%(str(self.__id))
                        printWithTime(message)
                        self.__gui.mouse_click_bg(position)
                        continue

            #check finish
            # position=self.__gui.find_game_img(IMAGE_REALM_FINISHED1_PATH,gray=0)
            # if position != False:
            #     printWithTime("Message: Account %s: Finishing..."%(str(self.__id)))
            #     self.__gui.mouse_click_bg(position)
            #     self.__gui.mouse_click_bg(position)
            #     self.__gui.mouse_click_bg(position)
            #     self.__gui.mouse_click_bg(position)
            #     continue
            #claim reward
            position=self.__gui.find_game_img(IMAGE_SOUL_STAT_PATH)
            if position != False:
                printWithTime("Message: Account %s: Claim reward... "%(str(self.__id)))
                self.__gui.mouse_click_bg((564, 503))
                self.__gui.mouse_click_bg((564, 503))
                self.__gui.mouse_click_bg((564, 503))
                self.__gui.mouse_click_bg((564, 503))
                continue
            #Fail
            position=self.__gui.find_game_img(IMAGE_REALM_FAILED_PATH,gray=0)
            if position != False:
                printWithTime("Message: Account %s: Failed... "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue
#
    def gameModeStory(self):
        global _fullShikigamiCount
        global _isPaused
        printWithTime("Message: Account %s: Game mode Exploration"%(str(self.__id)))

        while True:
            #Reward settlement
            if (self.__gui.find_game_img(IMAGE_STORY_BACK_PATH)!= False
                or self.__gui.find_game_img(IMAGE_STORY_REWARD_CONFIRMED_PATH) != False):
                position=self.__gui.find_game_img(IMAGE_STORY_GET_REWARD_PATH)
                if position != False:
                    printWithTime("Message: Account %s: Get reward.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)
                    continue

                position=self.__gui.find_game_img(IMAGE_STORY_REWARD_CONFIRMED_PATH)
                if position != False:
                    printWithTime("Message: Account%s: Confirm.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(CLAIM_REWARD)
                    continue

                position=self.__gui.find_game_img(IMAGE_STORY_SPIRIT_PATH,thread=0.7)
                if position != False:
                    printWithTime("Message: Account%s: Spirit found.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(CLAIM_REWARD)
                    continue

            #detect whether is in batte ?
            if self.__gui.find_game_img(IMAGE_STORY_CHERRY_CAKE_PATH,thread=0.8) != False:
                if self.__gui.find_game_img(IMAGE_STORY_ISINTEAM_PATH,thread=0.65) == False:
                    printWithTime("Message: Account %s: Team not detected, exit round.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(STORY_BACK_COORDINATE)
                    time.sleep(2)
                    self.__gui.mouse_click_bg(STORY_OK_COORDINATE,None)
                    time.sleep(1)
                    continue




            if self.__isCaptain:
                #=============================================check in battle=================================================

                if self.__gui.find_game_img(IMAGE_STORY_SEAL_TICKET_PATH,thread=0.6) != False:
                    printWithTime("Message: Account %s: In game battle not detected.... "%(str(self.__id)))
                    _localVariable.isInBattle = False
                else:
                    _localVariable.isInBattle = True

                #detect whether in room ?
                if self.__gui.find_game_img(IMAGE_SOUL_INROOM_PATH,thread=0.7) != False:
                        position=self.__gui.find_game_img(IMAGE_SOUL_INVITE_PATH,1,REGION_TEAM_INVITE_SOUL[0],REGION_TEAM_INVITE_SOUL[1],thread=0.7)
                        if position != False:
                            while True:
                                position=self.__gui.find_game_img(IMAGE_SOUL_INVITE_PATH,1,REGION_TEAM_INVITE_SOUL[0],REGION_TEAM_INVITE_SOUL[1],thread=0.7)
                                if position==False:
                                    break
                                else:
                                    self.__gui.mouse_click_bg(position)
                                    time.sleep(2)
                                    position=self.__gui.find_game_img(IMAGE_STORY_INVITATION_CONFIRMED_PATH)
                                    if position != False:
                                        printWithTime("Message: Account %s: Choosing teammate..... "%(str(self.__id)))
                                        position=self.__gui.find_game_img(IMAGE_STORY_TEAMMATE_PATH)
                                        if position != False:
                                            self.__gui.mouse_click_bg(position)
                                            time.sleep(1)
                                            self.__gui.mouse_click_bg(INVITE_MEMBER_SOUL_COORDINATE)
                                            time.sleep(1)
                                            self.__gui.mouse_click_bg(START_SOUL_COORDINATE)
                                            printWithTime("Message: Account %s: Invite teamate..... "%(str(self.__id)))
                                            time.sleep(2)
                                        else:
                                            count=6
                                            while count>0:
                                                count-=1
                                                printWithTime("Message: Account %s: Can't finding ig, re trying..... "%(str(self.__id)))
                                                position=self.__gui.find_game_img(IMAGE_STORY_TEAMMATE_PATH)
                                                if position != False:
                                                    self.__gui.mouse_click_bg(position)
                                                    time.sleep(1)
                                                    self.__gui.mouse_click_bg(INVITE_MEMBER_SOUL_COORDINATE)
                                                    time.sleep(1)
                                                    self.__gui.mouse_click_bg(START_SOUL_COORDINATE)
                                                    printWithTime("Message: Account %s: Sucessfully finding teammate, starting battle..... "%(str(self.__id)))
                                                    break
                                                if count>3:
                                                    self.__gui.mouse_drag_bg(SLIDE_FRIEND_LIST_SOUL[0],SLIDE_FRIEND_LIST_SOUL[1])
                                                else:
                                                    self.__gui.mouse_drag_bg(SLIDE_FRIEND_LIST_SOUL[1],SLIDE_FRIEND_LIST_SOUL[0])
                        else:
                            self.__gui.mouse_click_bg(START_SOUL_COORDINATE)
                            time.sleep(0.5)

                if self.__gui.find_game_img(IMAGE_STORY_CHERRY_CAKE_PATH) == False and _localVariable.isInBattle == False:
                    position=self.__gui.find_game_img(IMAGE_STORY_INVITE_PATH,thread=0.7)
                    if position != False:
                        _localVariable.isBossDetected=False
                        printWithTime("Message: Account %s: Invite Teamate to continue.... "%(str(self.__id)))
                        self.__gui.mouse_click_bg(position)
                        continue

                    time.sleep(2)
                    position=self.__gui.find_game_img(IMAGE_STORY_INVITATION_CONFIRMED_PATH,thread=0.7)
                    if position != False and self.__gui.find_game_img(IMAGE_STORY_APPROVE_PATH,thread=0.7) != False:
                        _localVariable.isBossDetected=False
                        printWithTime("Message: Account %s: Click OK..... "%(str(self.__id)))
                        self.__gui.mouse_click_bg(position)
                        time.sleep(1)
                        continue

                    if self.__gui.find_game_img(IMAGE_STORY_LIST_CHAPTER_PATH)  != False:
                        position=self.__gui.find_game_img(IMAGE_STORY_LAST_CHAPTER)
                        if position != False:
                            printWithTime("Message: Account %s: Entering last chapter.... "%(str(self.__id)))
                            self.__gui.mouse_click_bg(position)
                            continue

                    position=self.__gui.find_game_img(IMAGE_STORY_TEAM_PATH)
                    if  position == False and self.__gui.find_game_img(IMAGE_STORY_CREATE_PATH,thread=0.8)==False:
                        printWithTime("Message: Account %s: Choosing HARD level..... "%(str(self.__id)))
                        self.__gui.mouse_click_bg(CHOOSE_LEVEL_HARD_COORDINATE)
                        self.__gui.mouse_click_bg(CHOOSE_LEVEL_HARD_COORDINATE)
                        continue
                    else:
                        self.__gui.mouse_click_bg(TEAM_COORDINATE)
                        time.sleep(0.5)

                    position=self.__gui.find_game_img(IMAGE_STORY_CREATE_PATH,thread=0.8)
                    if position != False:
                        printWithTime("Message: Account %s: Create room..... "%(str(self.__id)))
                        self.__gui.mouse_click_bg(position)
                        continue


                #===============================================slide windows if not found monster
                if self.__gui.find_game_img(IMAGE_STORY_FIGHT_PATH) == False and self.__gui.find_game_img(IMAGE_STORY_CHERRY_CAKE_PATH) != False and self.__gui.find_game_img(IMAGE_STORY_FIGHT_BOSS_PATH) == False:
                    _localVariable.detectCount-=1
                    _localVariable.isInBattle = True
                    if self.__gui.find_game_img(IMAGE_STORY_FIGHT_PATH) == False and self.__gui.find_game_img(IMAGE_STORY_FIGHT_BOSS_PATH) == False:
                        if _localVariable.detectCount > 6:
                            self.__gui.mouse_drag_bg(SLIDE_STORY_COORDINATE[1],SLIDE_STORY_COORDINATE[0])
                        else:
                            self.__gui.mouse_drag_bg(SLIDE_STORY_COORDINATE[0],SLIDE_STORY_COORDINATE[1])
                        printWithTime("Message: Account %s: No Monster was detected..."%(str(self.__id)))
                        printWithTime("Message: Account %s: No Boss was detected..."%(str(self.__id)))
                        if _localVariable.detectCount==3:
                            _localVariable.detectCount=10


                position=self.__gui.find_game_img(IMAGE_STORY_FIGHT_BOSS_PATH)
                if position != False:
                    printWithTime("Message: Account %s: BOSS was detected%s: "%(str(self.__id),IMAGE_STORY_FIGHT_BOSS_PATH))
                    self.__gui.mouse_click_bg(position)
                    _localVariable.isBossDetected=True
                    _localVariable.isInBattle = True
                    continue

                position=self.__gui.find_game_img(IMAGE_STORY_FIGHT_PATH)
                if position != False:
                    printWithTime("Message: Account %s: Monster was detected..%s: "%(str(self.__id),IMAGE_STORY_FIGHT_PATH))
                    self.__gui.mouse_click_bg(position)
                    _localVariable.isInBattle = True
                    continue


                #=========================================replace shikigami=========================================
                if self.__isMainDMG==True:
                    #if Main dmg is leader
                    if _replaceShikigamiIfFull and self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_FIND_FULL_EXP_LEADER[0], \
                            REGION_FIND_FULL_EXP_LEADER[1], thread=0.7) != False:
                        printWithTime("Message: Account %s: Full-EXP shikigami was detected..."%(str(self.__id)))
                        def inner():
                            global _fullShikigamiCount
                            #ready
                            while self.__gui.find_game_img(IMAGE_STORY_READY_MARK_PATH) == False:
                                time.sleep(0.1)
                                continue

                            self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                            self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                            printWithTime("Message: Account %s: Changing shikigami..."%(str(self.__id)))
                            #change shikigami
                            while self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)==False:
                                self.__gui.mouse_click_bg(SHIKI_LEVEL_COORDINATE)
                                time.sleep(2)

                            position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                            while True:
                                if position == False:
                                    printWithTime("Message: Account %s: Failed to selecting type of shikigami, try again..."%(str(self.__id)))
                                    position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                                    continue

                                self.__gui.mouse_click_bg(position)
                                printWithTime("Message: Account %s: Selecting type of shikigami..."%(str(self.__id)))
                                if self.__gui.find_game_img(IMAGE_STORY_SELECT_LEVEL_PATH)==False:
                                    break

                            count=0
                            while count<2:
                                count+=1
                                while True:
                                    position=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED_PATH,thread=0.9)
                                    sel1=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED1_PATH,thread=0.9)
                                    sel2=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED2_PATH,thread=0.9)
                                    sel3=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED3_PATH,thread=0.9)
                                    sel8=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED8_PATH,thread=0.9)
                                    if position or sel1 or sel2 or sel3 or sel8:
                                        break
                                    self.__gui.mouse_drag_bg(SLIDE_CHANGE_SHIKI[1],SLIDE_CHANGE_SHIKI[0])


                                printWithTime("Message: Account %s: Shikigami was found..."%(str(self.__id)))
                                position1=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_FULL_EXP_LEADER[0],REGION_CHANGE_FULL_EXP_LEADER[1],thread=0.7)
                                if position1 != False:
                                    if position != False:
                                        self.__gui.mouse_drag_bg(position,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel1 != False:
                                        self.__gui.mouse_drag_bg(sel1,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel2 != False:
                                        self.__gui.mouse_drag_bg(sel2,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel3 != False:
                                        self.__gui.mouse_drag_bg(sel3,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel8 != False:
                                        self.__gui.mouse_drag_bg(sel8,(position1[0],position1[1]+30),delay=0.1)
                                    time.sleep(0.5)


                                positionTmp=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_FIND_FULL_EXP_LEADER[0],REGION_FIND_FULL_EXP_LEADER[1],thread=0.8)
                                if position1!=positionTmp:
                                    _fullShikigamiCount+=1
                                    printWithTime("Message: Account %s: Shikigami has been replaced..."%(str(self.__id)))

                                if self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_FIND_FULL_EXP_LEADER[0],REGION_FIND_FULL_EXP_LEADER[1],thread=0.8)==False:
                                    printWithTime("Message: Account %s: Completed, no full-exp Shikigami was found..."%(str(self.__id)))
                                    break

                        innerThread=threading.Thread(None,inner,str(self.__id))
                        innerThread.start()
                        winsound.Beep(1000,3000)
                        seconds=30
                        while seconds and not innerThread.is_alive():
                            time.sleep(1.0)
                            seconds-=1

                        seconds=30
                        while seconds and innerThread.is_alive():
                            printWithTime("Message: Account %s: Waiting for food to replace"%(str(self.__id)))
                            time.sleep(1.0)
                            seconds-=1
                        stopThread(innerThread)
                        if not _isPaused:
                            self.__thread.threadGameRelease()
                else:
                    if _replaceShikigamiIfFull and self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,thread=0.7) != False:
                        printWithTime("Message: Account %s: Full-EXP shikigami was detected..."%(str(self.__id)))
                        def inner():
                            global _fullShikigamiCount
                            #ready
                            while self.__gui.find_game_img(IMAGE_STORY_READY_MARK_PATH) == False:
                                time.sleep(0.1)
                                continue

                            self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                            self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                            printWithTime("Message: Account %s: Changing shikigami..."%(str(self.__id)))
                            #change shikigami
                            while self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)==False:
                                self.__gui.mouse_click_bg(SHIKI_LEVEL_COORDINATE)
                                time.sleep(2)

                            position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                            while True:
                                if position == False:
                                    printWithTime("Message: Account %s: Failed to selecting type of shikigami, try again..."%(str(self.__id)))
                                    position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                                    continue

                                self.__gui.mouse_click_bg(position)
                                printWithTime("Message: Account %s: Selecting type of shikigami..."%(str(self.__id)))
                                if self.__gui.find_game_img(IMAGE_STORY_SELECT_LEVEL_PATH)==False:
                                    break

                            count=0
                            while count<2:
                                sel2=False
                                count+=1
                                while True:
                                    position=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED_PATH,thread=0.9)
                                    sel1=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED1_PATH,thread=0.9)
                                    sel2=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED2_PATH,thread=0.9)
                                    sel3=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED3_PATH,thread=0.9)
                                    sel8=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED8_PATH,thread=0.9)
                                    if position or sel1 or sel2 or sel3 or sel8:
                                        break
                                    self.__gui.mouse_drag_bg(SLIDE_CHANGE_SHIKI[1],SLIDE_CHANGE_SHIKI[0])



                                printWithTime("Message: Account %s: Shikigami was found..."%(str(self.__id)))
                                position1=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,(0,0),(1100,350),thread=0.7)
                                if position1 != False:
                                    if position != False:
                                        self.__gui.mouse_drag_bg(position,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel1 != False:
                                        self.__gui.mouse_drag_bg(sel1,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel2 != False:
                                        self.__gui.mouse_drag_bg(sel2,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel3 != False:
                                        self.__gui.mouse_drag_bg(sel3,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel8 != False:
                                        self.__gui.mouse_drag_bg(sel8,(position1[0],position1[1]+30),delay=0.1)

                                    time.sleep(0.5)



                                positionTmp=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,(0,0),(1100,350),thread=0.7)
                                if position1!=positionTmp:
                                    _fullShikigamiCount+=1
                                    printWithTime("Message: Account %s: Shikigami has been replaced..."%(str(self.__id)))

                                if self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,(0,0),(1100,350),thread=0.7)==False:
                                    printWithTime("Message: Account %s: Completed, no full-exp Shikigami was found..."%(str(self.__id)))
                                    break

                        innerThread=threading.Thread(None,inner,str(self.__id))
                        innerThread.start()
                        winsound.Beep(1000,3000)
                        seconds=30
                        while seconds and not innerThread.is_alive():
                            time.sleep(1.0)
                            seconds-=1

                        seconds=30
                        while seconds and innerThread.is_alive():
                            printWithTime("Message: Account %s: Waiting for food to replace"%(str(self.__id)))
                            time.sleep(1.0)
                            seconds-=1
                        stopThread(innerThread)
                        if not _isPaused:
                            self.__thread.threadGameRelease()


                #=========================================get ready=================================================

                position=self.__gui.find_game_img(IMAGE_STORY_READY_PATH,thread=0.8)
                if position != False:
                    printWithTime("Message: Account %s: Starting battle.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)
                    #time.sleep(2)
                    continue

                #=========================================Finish=================================================

                position=self.__gui.find_game_img(IMAGE_STORY_FINISHED1_PATH)
                if position != False:
                    printWithTime("Message: Account %s: Finishing.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)
                    continue

                position=self.__gui.find_game_img(IMAGE_STORY_FINISHED2_PATH)
                if position != False:
                    printWithTime("Message: Account %s: Finished.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)

                    while True:
                        if self.__gui.find_game_img(IMAGE_STORY_FINISHED2_PATH)== False:
                            break
                        self.__gui.mouse_click_bg(position)
                        printWithTime("Message: Account %s: Get reward.... position"%(str(self.__id)))
                    break
            else:
                 #=========================================replace shikigami=========================================

                if self.__isMainDMG==False:
                    if _replaceShikigamiIfFull and self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,thread=0.7) != False:
                        printWithTime("Message: Account %s: Full-EXP shikigami was detected..."%(str(self.__id)))
                        def inner():
                            global _fullShikigamiCount
                            #ready
                            while self.__gui.find_game_img(IMAGE_STORY_READY_MARK_PATH) == False:
                                time.sleep(0.1)
                                continue

                            self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                            self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                            printWithTime("Message: Account %s: Changing shikigami..."%(str(self.__id)))
                            #change shikigami
                            while self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)==False:
                                self.__gui.mouse_click_bg(SHIKI_LEVEL_COORDINATE)
                                time.sleep(2)

                            position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                            while True:
                                if position == False:
                                    printWithTime("Message: Account %s: Failed to selecting type of shikigami, try again..."%(str(self.__id)))
                                    position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                                    continue

                                self.__gui.mouse_click_bg(position)
                                printWithTime("Message: Account %s: Selecting type of shikigami..."%(str(self.__id)))
                                if self.__gui.find_game_img(IMAGE_STORY_SELECT_LEVEL_PATH)==False:
                                    break

                            count=0
                            while count<3:
                                count+=1
                                sel2=False
                                while True:
                                    position=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED_PATH,thread=0.9)
                                    sel1=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED1_PATH,thread=0.9)
                                    sel2=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED2_PATH,thread=0.9)
                                    sel3=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED3_PATH,thread=0.9)
                                    sel8=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED8_PATH,thread=0.9)
                                    if position != False or sel2 != False:
                                        break
                                    self.__gui.mouse_drag_bg(SLIDE_CHANGE_SHIKI[1],SLIDE_CHANGE_SHIKI[0])


                                printWithTime("Message: Account %s: Shikigami was found..."%(str(self.__id)))
                                position1=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_FULL_EXP_PASENGER[0],REGION_CHANGE_FULL_EXP_PASENGER[1],thread=0.7)
                                if position1 != False:
                                    if position != False:
                                        self.__gui.mouse_drag_bg(position,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel1 != False:
                                        self.__gui.mouse_drag_bg(sel1,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel2 != False:
                                        self.__gui.mouse_drag_bg(sel2,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel3 != False:
                                        self.__gui.mouse_drag_bg(sel3,(position1[0],position1[1]+30),delay=0.1)

                                    elif sel8 != False:
                                        self.__gui.mouse_drag_bg(sel8,(position1[0],position1[1]+30),delay=0.1)
                                    time.sleep(0.5)


                                positionTmp=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_FULL_EXP_PASENGER[0],REGION_CHANGE_FULL_EXP_PASENGER[1],thread=0.8)
                                if position1!=positionTmp:
                                    _fullShikigamiCount+=1
                                    printWithTime("Message: Account %s: Shikigami has been replaced..."%(str(self.__id)))

                                if self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_FULL_EXP_PASENGER[0],REGION_CHANGE_FULL_EXP_PASENGER[1],thread=0.8)==False:
                                    printWithTime("Message: Account %s: Completed, no full-exp Shikigami was found..."%(str(self.__id)))
                                    break


                        innerThread=threading.Thread(None,inner,str(self.__id))
                        innerThread.start()
                        winsound.Beep(1000,3000)
                        seconds=30
                        while seconds and not innerThread.is_alive():
                            time.sleep(1.0)
                            seconds-=1

                        seconds=30
                        while seconds and innerThread.is_alive():
                            printWithTime("Message: Account %s: Waiting for food to replace..."%(str(self.__id)))
                            time.sleep(1.0)
                            seconds-=1
                        stopThread(innerThread)
                        if not _isPaused:
                            self.__thread.threadGameRelease()
                else:
                    if _replaceShikigamiIfFull and self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_FIND_FULL_EXP_SOLO[0],REGION_FIND_FULL_EXP_SOLO[1],thread=0.75) != False:
                        printWithTime("Message: Account %s: Full-EXP shikigami was detected..."%(str(self.__id)))
                        def inner():
                            global _fullShikigamiCount
                            #ready
                            while self.__gui.find_game_img(IMAGE_STORY_READY_MARK_PATH) == False:
                                time.sleep(0.1)
                                continue

                            self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                            self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                            printWithTime("Message: Account %s: Changing shikigami..."%(str(self.__id)))
                            #change shikigami
                            while self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)==False:
                                self.__gui.mouse_click_bg(SHIKI_LEVEL_COORDINATE)
                                time.sleep(2)

                            position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                            while True:
                                if position == False:
                                    printWithTime("Message: Account %s: Failed to selecting type of shikigami, try again..."%(str(self.__id)))
                                    position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                                    continue

                                self.__gui.mouse_click_bg(position)
                                printWithTime("Message: Account %s: Selecting type of shikigami..."%(str(self.__id)))
                                if self.__gui.find_game_img(IMAGE_STORY_SELECT_LEVEL_PATH)==False:
                                    break

                            count=0
                            while count<3:
                                count+=1
                                while True:
                                    position=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED_PATH,thread=0.9)
                                    sel1=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED1_PATH,thread=0.9)
                                    sel2=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED2_PATH,thread=0.9)
                                    sel3=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED3_PATH,thread=0.9)
                                    sel8=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED8_PATH,thread=0.9)
                                    if position or sel1 or sel2 or sel3 or sel8:
                                        break
                                    self.__gui.mouse_drag_bg(SLIDE_CHANGE_SHIKI[1],SLIDE_CHANGE_SHIKI[0])


                                printWithTime("Message: Account %s: Shikigami was found..."%(str(self.__id)))
                                position1=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_EXP_SOLO[0],REGION_CHANGE_EXP_SOLO[1],thread=0.7)
                                if position1 != False:
                                    X=REGION_CHANGE_EXP_SOLO[0][0]+position1[0]
                                    Y=REGION_CHANGE_EXP_SOLO[0][1]+position1[1]
                                    if position !=False:
                                        self.__gui.mouse_drag_bg(position,(X,Y))
                                    elif sel1 !=False:
                                        self.__gui.mouse_drag_bg(sel1,(X,Y))
                                    elif sel2 !=False:
                                        self.__gui.mouse_drag_bg(sel2,(X,Y))
                                    elif sel3 !=False:
                                        self.__gui.mouse_drag_bg(sel3,(X,Y))
                                    elif sel8 !=False:
                                        self.__gui.mouse_drag_bg(sel8,(X,Y))

                                    time.sleep(0.5)


                                positionTmp=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_EXP_SOLO[0],REGION_CHANGE_EXP_SOLO[1],thread=0.8)
                                if position1!=positionTmp:
                                    _fullShikigamiCount+=1
                                    printWithTime("Message: Account %s: Shikigami has been replaced..."%(str(self.__id)))

                                if self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_EXP_SOLO[0],REGION_CHANGE_EXP_SOLO[1],thread=0.8)==False:
                                    printWithTime("Message: Account %s: Completed, no full-exp Shikigami was found..."%(str(self.__id)))
                                    break


                        innerThread=threading.Thread(None,inner,str(self.__id))
                        innerThread.start()
                        winsound.Beep(1000,3000)
                        seconds=30
                        while seconds and not innerThread.is_alive():
                            time.sleep(1.0)
                            seconds-=1

                        seconds=30
                        while seconds and innerThread.is_alive():
                            printWithTime("Message: Account %s: Waiting for food to replace"%(str(self.__id)))
                            time.sleep(1.0)
                            seconds-=1
                        stopThread(innerThread)
                        if not _isPaused:
                            self.__thread.threadGameRelease()

               #=========================================get ready=================================================
                position=self.__gui.find_game_img(IMAGE_STORY_READY_PATH,thread=0.7)
                if position != False:
                    printWithTime("Message: Account %s: Starting battle.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)
                    #time.sleep(2)
                    continue

                #=========================================Finish=================================================

                position=self.__gui.find_game_img(IMAGE_STORY_FINISHED1_PATH)
                if position != False:
                    printWithTime("Message: Account %s: Finishing.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)
                    continue

                position=self.__gui.find_game_img(IMAGE_STORY_FINISHED2_PATH)
                if position != False:
                    printWithTime("Message: Finish2%s: Finished.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)

                    while True:
                        if self.__gui.find_game_img(IMAGE_STORY_FINISHED2_PATH)== False:
                            break
                        self.__gui.mouse_click_bg(position)
                        printWithTime("Message: Account %s: Get reward...."%(str(self.__id)))
                    break

                position=self.__gui.find_game_img(IMAGE_STORY_ACCEPT_PATH,thread=0.7)
                if position != False:
                    message="Message: Account %s: Tried to accept a new round Chapter Exploration..."%(str(self.__id))
                    printWithTime(message)
                    self.__gui.mouse_click_bg(position)
                    continue
#
    def gameModeSingleStory(self):
        global _fullShikigamiCount
        global _isPaused
        printWithTime("Message: Account %s: Game mode Exploration"%(str(self.__id)))
        while True:
            #self.__gui.rejectbounty()
            #printWithTime("Message: Account %s: Checking co-op wanted..."%(str(self.__id)))
            if self.__gui.find_game_img(IMAGE_STORY_CHERRY_CAKE_PATH) == False:
                position=self.__gui.find_game_img(IMAGE_STORY_LAST_CHAPTER)
                if position != False:
                    _localVariable.isBossDetected=False
                    printWithTime("Message: Account %s: Entering last chapter.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)
                    continue


                position=self.__gui.find_game_img(IMAGE_STORY_START_PATH)
                if position != False:
                    _localVariable.isBossDetected=False
                    printWithTime("Message: Account %s: Starting exploration.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)
                    continue

            if self.__gui.find_game_img(IMAGE_STORY_FIGHT_PATH) == False and self.__gui.find_game_img(IMAGE_STORY_CHERRY_CAKE_PATH) != False and self.__gui.find_game_img(IMAGE_STORY_FIGHT_BOSS_PATH) == False:
                _localVariable.detectCount-=1
                if self.__gui.find_game_img(IMAGE_STORY_FIGHT_PATH) == False and self.__gui.find_game_img(IMAGE_STORY_FIGHT_BOSS_PATH) == False:
                    if _localVariable.detectCount > 5:
                        self.__gui.mouse_drag_bg(SLIDE_STORY_COORDINATE[1],SLIDE_STORY_COORDINATE[0])
                    else:
                        self.__gui.mouse_drag_bg(SLIDE_STORY_COORDINATE[0],SLIDE_STORY_COORDINATE[1])
                    printWithTime("Message: Account %s: No Monster was detected..."%(str(self.__id)))
                    printWithTime("Message: Account %s: No Boss was detected..."%(str(self.__id)))
                    if _localVariable.detectCount==2:
                        _localVariable.detectCount=10

            position=self.__gui.find_game_img(IMAGE_STORY_FIGHT_PATH)
            if position != False:
                printWithTime("Message: Account %s: Monster was detected... "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue

            position=self.__gui.find_game_img(IMAGE_STORY_FIGHT_BOSS_PATH)
            if position != False:
                printWithTime("Message: Account %s: BOSS was detected: "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                _localVariable.isBossDetected=True
                continue

            #=========================================replace shikigami=========================================

            if _replaceShikigamiIfFull and self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_FIND_FULL_EXP_SOLO[0],REGION_FIND_FULL_EXP_SOLO[1]) != False:
                printWithTime("Message: Account %s: Full-EXP shikigami was detected..."%(str(self.__id)))
                def inner():
                    global _fullShikigamiCount
                    #ready
                    while self.__gui.find_game_img(IMAGE_STORY_READY_MARK_PATH) == False:
                        time.sleep(0.1)
                        continue

                    self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                    self.__gui.mouse_click_bg(CHANGE_SHIKI_COORDINATE)
                    printWithTime("Message: Account %s: Changing shikigami..."%(str(self.__id)))
                    #change shikigami
                    while self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)==False:
                        self.__gui.mouse_click_bg(SHIKI_LEVEL_COORDINATE)
                        time.sleep(2)

                    position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                    while True:
                        if position == False:
                            printWithTime("Message: Account %s: Failed to selecting type of shikigami, try again..."%(str(self.__id)))
                            position=self.__gui.find_game_img(IMAGE_STORY_SELECTED_LEVEL_PATH)
                            continue

                        self.__gui.mouse_click_bg(position)
                        printWithTime("Message: Account %s: Selecting type of shikigami..."%(str(self.__id)))
                        if self.__gui.find_game_img(IMAGE_STORY_SELECT_LEVEL_PATH)==False:
                            break

                    count=0
                    while count<3:
                        count+=1
                        while True:
                            position=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED_PATH,thread=0.9)
                            sel1=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED2_PATH,thread=0.9)
                            sel2=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED2_PATH,thread=0.9)
                            sel3=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED2_PATH,thread=0.9)
                            sel8=self.__gui.find_game_img(IMAGE_STORY_SHIKIGAMI_SELECTED2_PATH,thread=0.9)
                            if position or sel1 or sel2 or sel3 or sel8:
                                break
                            self.__gui.mouse_drag_bg(SLIDE_CHANGE_SHIKI[1],SLIDE_CHANGE_SHIKI[0])


                        printWithTime("Message: Account %s: Shikigami was found..."%(str(self.__id)))
                        position1=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_EXP_SOLO[0],REGION_CHANGE_EXP_SOLO[1],thread=0.7)
                        if position1 != False:
                            X=REGION_CHANGE_EXP_SOLO[0][0]+position1[0]
                            Y=REGION_CHANGE_EXP_SOLO[0][1]+position1[1]
                            if position !=False:
                                self.__gui.mouse_drag_bg(position,(X,Y))
                            elif sel1 !=False:
                                self.__gui.mouse_drag_bg(sel1,(X,Y))
                            elif sel2 !=False:
                                self.__gui.mouse_drag_bg(sel2,(X,Y))
                            elif sel3 !=False:
                                self.__gui.mouse_drag_bg(sel3,(X,Y))
                            elif sel8 !=False:
                                self.__gui.mouse_drag_bg(sel8,(X,Y))
                            time.sleep(0.5)


                        positionTmp=self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_EXP_SOLO[0],REGION_CHANGE_EXP_SOLO[1],thread=0.8)
                        if position1!=positionTmp:
                            _fullShikigamiCount+=1
                            printWithTime("Message: Account %s: Shikigami has been replaced..."%(str(self.__id)))

                        if self.__gui.find_game_img(IMAGE_STORY_FULL1_PATH,1,REGION_CHANGE_EXP_SOLO[0],REGION_CHANGE_EXP_SOLO[1],thread=0.8)==False:
                            printWithTime("Message: Account %s: Completed, no full-exp Shikigami was found..."%(str(self.__id)))
                            break


                innerThread=threading.Thread(None,inner,str(self.__id))
                innerThread.start()
                winsound.Beep(1000,3000)
                seconds=30
                while seconds and not innerThread.is_alive():
                    time.sleep(1.0)
                    seconds-=1

                seconds=30
                while seconds and innerThread.is_alive():
                    printWithTime("Message: Account %s: Waiting for food to replace"%(str(self.__id)))
                    time.sleep(1.0)
                    seconds-=1
                stopThread(innerThread)
                if not _isPaused:
                    self.__thread.threadGameRelease()


            #=========================================get ready=================================================

            position=self.__gui.find_game_img(IMAGE_STORY_READY_PATH,gray=0,thread=0.8)
            if position != False:
                printWithTime("Message: Account %s: Starting battle.... "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                #time.sleep(2)
                continue

            #=========================================Finish=================================================

            position=self.__gui.find_game_img(IMAGE_STORY_FINISHED1_PATH)
            if position != False:
                printWithTime("Message: Account %s: Finishing.... "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue

            position=self.__gui.find_game_img(IMAGE_STORY_FINISHED2_PATH)
            if position != False:
                printWithTime("Message: Account %s: Finished... "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)

                while True:
                    if self.__gui.find_game_img(IMAGE_STORY_FINISHED2_PATH)== False:
                        break
                    self.__gui.mouse_click_bg(position)
                    printWithTime("Message: Account %s: Get reward..."%(str(self.__id)))
                break

            #==========================================Reward settlement=============================================
            if (self.__gui.find_game_img(IMAGE_STORY_BACK_PATH)!= False
                or self.__gui.find_game_img(IMAGE_STORY_REWARD_CONFIRMED_PATH) != False):
                position=self.__gui.find_game_img(IMAGE_STORY_GET_REWARD_PATH)
                if position != False:
                    printWithTime("Message: Account %s: Get treasure.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(position)

                position=self.__gui.find_game_img(IMAGE_STORY_REWARD_CONFIRMED_PATH)
                if position != False:
                    printWithTime("Message: Account%s: Confirm.... "%(str(self.__id)))
                    self.__gui.mouse_click_bg(CLAIM_REWARD)
#
    def gameModeRealmRaid(self):
        printWithTime("Message: Account %s: Realm Raid mode, make sure to set up your lineup before starting...."%(str(self.__id)))
        while True:
            position=self.__gui.find_game_img(IMAGE_REALM_PROFILE_PATH,thread=0.85)
            if position != False:
                printWithTime("Message: Account %s: In battle detected, sleep 5s ..."%(str(self.__id)))
                time.sleep(5)
                continue

            #Click icon realm
            position=self.__gui.find_game_img(IMAGE_REALM_RAID_PATH)
            if position != False:
                printWithTime("Message: Account %s: Click icon realm raid..."%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue

            #not enough ticket
            if self.__gui.find_game_img(IMAGE_REALM_EMPTY_TICKET,thread=0.97) !=False:
                printWithTime("Message: Account %s: DONE... "%(str(self.__id)))
                pyautogui.alert(text='REALM RAID DONE', title='FINISH', button='OK')
                sys.exit()
                break

            #lock line up
            position=self.__gui.find_game_img(IMAGE_REALM_LOCK_PATH)
            if position != False:
                printWithTime("Message: Account %s: Successfully lock lineup..."%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue

            #Click Realm
            position=self.__gui.find_game_img(IMAGE_REALM_SECTION_PATH,thread=0.7)
            if position != False:
                self.__gui.mouse_click_bg(position)
                printWithTime("Message: Account %s: Enemy was found..."%(str(self.__id)))
                time.sleep(1)
                self.__gui.mouse_click_bg((position[0]-77,position[1]+144))
                #time.sleep(15)
                continue


            #check finish
            position=self.__gui.find_game_img(IMAGE_REALM_FINISHED1_PATH,gray=0)
            if position != False:
                printWithTime("Message: Account %s: Finishing..."%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue

            position=self.__gui.find_game_img(IMAGE_REALM_FINISHED2_PATH,thread=0.7)
            if position != False:
                printWithTime("Message: Account %s: Getting reward... "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)

                while True:
                    if self.__gui.find_game_img(IMAGE_REALM_FINISHED2_PATH,thread=0.7) == False:
                        break
                    self.__gui.mouse_click_bg(position)
                break

            #Fail
            position=self.__gui.find_game_img(IMAGE_REALM_FAILED_PATH,gray=0)
            if position != False:
                printWithTime("Message: Account %s: Failed, Enemy is very strong... "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue

            #Refresh if can not fight

            if self.__gui.find_game_img(IMAGE_REALM_SECTION_PATH,thread=0.6) == False and self.__gui.find_game_img(IMAGE_REALM_RANK_PATH,thread=1, gray=0) != False:
                printWithTime("Message: Account %s: Enemy is very strong, refresh to get new turn... "%(str(self.__id)))
                pyautogui.alert(text='Refresh new turn...', title='Realm raid', button='OK')
                # position=self.__gui.find_game_img(IMAGE_REALM_REFRESH_PATH,gray=0)
                # self.__gui.mouse_click_bg(position)
                continue
#
    def gameModeDemonSeal(self):
        printWithTime("Message: Account :%s: Fairy Seal"%(str(self.__id)))
        while True:
            position=self.__gui.find_game_img(IMAGE_SEAL_WAIT_PATH,thread=0.8)
            if position != False:
                printWithTime("Message: Account :%s: Finding team, sleep 10s..."%(str(self.__id)))
                time.sleep(10)
                continue

            position=self.__gui.find_game_img(IMAGE_STORY_READY_PATH,gray=0,thread=0.8)
            if position != False:
                printWithTime("Message: Account %s: Ready for battle.... "%(str(self.__id)))
                time.sleep(5)
                self.__gui.mouse_click_bg(position)
                #time.sleep(2)
                continue

            position=self.__gui.find_game_img(IMAGE_REALM_PROFILE_PATH,thread=0.85)
            if position != False:
                printWithTime("Message: Account %s: In battle detected, sleep 5s ..."%(str(self.__id)))
                time.sleep(5)
                continue

            position=self.__gui.find_game_img(IMAGE_SEAL_TEAM_PATH)
            if position != False:
                printWithTime("Message: Account :%s: Clicking team icon..."%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue

            position=self.__gui.find_game_img(IMAGE_SEAL_MATCH_PATH)
            if position != False:
                printWithTime("Message: Account :%s: Matching..."%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                time.sleep(1)
                continue


            # if self.__gui.find_game_img(IMAGE_SEAL_REFRESH_PATH) != False:
            #     while True:
            #         self.__gui.mouse_click_bg(REFRESH_SEAL_COORDINATE)
            #         time.sleep(0.5)
            #         position=self.__gui.find_game_img(IMAGE_SEAL_JOIN_PATH)
            #         if position != False:
            #             self.__gui.mouse_click_bg(position)
            #             self.__gui.mouse_click_bg(position)
            #             self.__gui.mouse_click_bg(position)
            #             printWithTime("Message: Account :%s: Click to join..."%(str(self.__id)))
            #             break



            #check finish
            position=self.__gui.find_game_img(IMAGE_REALM_FINISHED1_PATH,gray=0)
            if position != False:
                printWithTime("Message: Account %s: Finishing..."%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue

            position=self.__gui.find_game_img(IMAGE_REALM_FINISHED2_PATH)
            if position != False:
                printWithTime("Message: Account %s: Getting reward... "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)

                while True:
                    if self.__gui.find_game_img(IMAGE_REALM_FINISHED2_PATH) == False:
                        break
                    self.__gui.mouse_click_bg(position)
                break

            position=self.__gui.find_game_img(IMAGE_SOUL_START_PATH,gray=0)
            if position != False:
                printWithTime("Message: Account %s: Starting game... "%(str(self.__id)))
                self.__gui.mouse_click_bg(position)
                continue
#
    def gameModeEvent(self):
        while True:
            self.targetShikigami()
#

    def detectPause(self):
        global _isPaused
        while True:
            keyboard.wait(hotkey='f1')
            printWithTime("Message: F1 was pressed")
            #self.__gui.quit_game()
            if _isPaused:
                _isPaused=False
                _accountLocker.release()
                printWithTime("Continued")
            else:
                _isPaused=True
                _accountLocker.acquire()
                printWithTime("Paused")
#
    def detectAssistance(self):

        while True:
            time.sleep(10)
            message="Message: Account %s: Checking co-op wanted seal..."%(str(self.__id))
            printWithTime(message)

            coop=self.__gui.find_game_img(IMAGE_COOP_SEAL,thread=0.8)
            if coop == False:
                continue

            message="Message: Account %s: An invitation for a wanted seal was detected..."%(str(self.__id))
            printWithTime(message)


            message="Message: Account %s: Refuse to accept the invitation for the wanted seal..."%(str(self.__id))
            printWithTime(message)
            self.__gui.mouse_click_bg((750, 452))
#
    def targetShikigami(self,location=None):
        while True:
            message="Message: Account %s: Begin check target shikigami..."%(str(self.__id))
            printWithTime(message)
            profile=self.__gui.find_game_img(IMAGE_REALM_PROFILE_PATH,thread=0.8)
            set=self.__gui.find_game_img(IMAGE_SOUL_SET_PATH,thread=0.8)
            if profile!=False and set==False:
                while True:
                    profile=self.__gui.find_game_img(IMAGE_REALM_PROFILE_PATH,thread=0.8)
                    target=self.__gui.find_game_img(IMAGE_TARGET_SHIKIGAMI,thread=0.8)
                    if target==False and profile!=False:
                        message="Message: Account %s: Target to the 5th shikigami..."%(str(self.__id))
                        printWithTime(message)
                        seductress_soul = self.__gui.find_game_img(IMAGE_SOUL_SEDUCTRESS, thread=0.8)
                        ghostly_soul=self.__gui.find_game_img(IMAGE_SOUL_GHOSTLY,thread=0.8)

                        if not seductress_soul or not ghostly_soul:
                            self.__gui.mouse_click_bg((150, 423))
                            time.sleep(1)
                    
                    if target!=False and profile!=False:
                        while self.isInBattle():
                            printWithTime("Message: Account %s: In battle detected, sleep 5s ..."%(str(self.__id)))
                            time.sleep(5)
                        break
            else:
                time.sleep(5)


    def claimRewardBattle(self):
        position=self.__gui.find_game_img(IMAGE_STORY_FINISHED1_PATH)
        if position != False:
            printWithTime("Message: Account %s: Finishing.... "%(str(self.__id)))
            self.__gui.mouse_click_bg(position)


        position=self.__gui.find_game_img(IMAGE_STORY_FINISHED2_PATH)
        if position != False:
            printWithTime("Message: Account %s: Finished.... "%(str(self.__id)))
            self.__gui.mouse_click_bg(position)
            while True:
                if self.__gui.find_game_img(IMAGE_STORY_FINISHED2_PATH)== False:
                    break
                self.__gui.mouse_click_bg(position)
                printWithTime("Message: Account %s: Get reward.... position"%(str(self.__id)))

    def isInBattle(self):
        position=self.__gui.find_game_img(IMAGE_REALM_PROFILE_PATH,thread=0.85)
        if position != False or self.__gui.find_game_img(IMAGE_SOUL_SET_PATH,thread=0.8) != False:
            return True
        return False


    def run(self):
        _localVariable.isBossDetected=False
        _localVariable.isInBattle=False
        _localVariable.isInRoom=False
        _localVariable.detectCount=10
        count=0
        while self.__total-count>0:
            seconds=0
            while seconds:
                time.sleep(1)
                seconds-=1
            printWithTime("\n\n==============Account %s: "%(str(self.__id))+"Starting a new round==================")
            if self.__gameMode==1:
                self.gameModeSoul()
            elif self.__gameMode==2:
                _localVariable.detectCount=10
                _localVariable.xDirection=-1.0
                self.gameModeStory()
            elif self.__gameMode==3:
                self.gameModeSingleStory()
            elif self.__gameMode==4:
                self.gameModeRealmRaid()
            elif self.__gameMode==5:
                self.gameModeDemonSeal()
            elif self.__gameMode==6:
                self.gameModeEvent()
            count+=1
            message="Account %s: Game mode %s, completed %s round, remaining %s round..."%(str(self.__id),str(self.__gameMode),str(count),str(self.__total-count))
            printWithTime(message)

