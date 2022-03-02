class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        # to amount for the movement
        # since robot faces north so move ahed will be 1 unit on y axis
        dirx,diry = 0,1
        x,y = 0,0 # to mark positions of robot(current origin)
        
        for instruction in instructions:
            if instruction == "G":
                x,y = x+dirx,y+diry # since we move forward
            
            elif instruction == "L":
                dirx,diry = -diry,dirx # since when we turn left -y axis becoomes our x axis
            
            else:
                dirx,diry = diry, -dirx
        
        # if we get back to origin or we have change in direction
        return (x,y) == (0,0) or (dirx,diry)!=(0,1)
        