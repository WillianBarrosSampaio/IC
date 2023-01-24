import sim
import numpy as np

def connect(port):

    sim.simxFinish(-1) 
    clientID=sim.simxStart('127.0.0.1',port,True,True,2000,5) 
    if clientID == 0: print("conectado a", port)
    else: print("Sem conexão")
    return clientID

clientID = connect(19999)

name_handle = "Dummy"
name_axis1 = "MTB_joint1"
name_axis2 = "MTB_joint2"
name_axis3 = "MTB_joint3"

returnCode,handle=sim.simxGetObjectHandle(clientID,name_handle,sim.simx_opmode_blocking)
returnCode,joint1=sim.simxGetObjectHandle(clientID,name_axis1,sim.simx_opmode_blocking)
returnCode,joint2=sim.simxGetObjectHandle(clientID,name_axis2,sim.simx_opmode_blocking)
returnCode,joint3=sim.simxGetObjectHandle(clientID,name_axis3,sim.simx_opmode_blocking)

dummy = handle

print(handle, joint1, joint2, joint3)

returnCode,pos=sim.simxGetObjectPosition(clientID, dummy, -1, sim.simx_opmode_blocking)
print(pos)

returnCode, pos1 = sim.simxGetJointPosition(clientID, joint1, sim.simx_opmode_blocking)
print(pos1)

returnCode, pos2 = sim.simxGetJointPosition(clientID, joint2, sim.simx_opmode_blocking)
print(pos2)


#teste dos valores
q1 = 0 * np.pi/180
q2 = 0 * np.pi/180
q3 = 0.2

#enviando dados para o robô
retCode = sim.simxSetJointTargetPosition(clientID, joint1, q1, sim.simx_opmode_oneshot)
retCode = sim.simxSetJointTargetPosition(clientID, joint2, q2, sim.simx_opmode_oneshot)
retCode = sim.simxSetJointTargetPosition(clientID, joint3, q3, sim.simx_opmode_oneshot)

