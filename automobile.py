from Hdmap import Hdmap


class automoile:
    storedHdmap: Hdmap = None;
    GTX = None;
    GTY = None;

    NNode = None;
    NNodeDist = None;
    SNode = None;
    SNodeDist = None;
    WNode = None;
    WNodeDist = None;
    ENode = None;
    ENodeDist = None;
    NENode = None;
    NENodeDist = None;
    SENode = None;
    SENodeDist = None;
    SWNode = None;
    SWNodeDist = None;
    NWNode = None;
    NWNodeDist = None;

    def lidar(self):
        if self.storedHdmap.get(self.GTX,self.GTY) is not None:
            print("You crushed?")
            print(self.storedHdmap.get(self.GTX,self.GTY))
            raise Exception
        # 看前面
        probeX = self.GTX
        probeY = self.GTY
        while probeY <= 11:
            if probeY == 11:
                print("Nothing in front.")
                exit("lost detection")
                break
            if self.storedHdmap.get(probeX,probeY) is not None:
                self.NNode = self.storedHdmap.getnode(probeX,probeY)
                self.NNodeDist = probeY - self.GTY
                print("Object in front detected: " + self.NNode.landmark + ", " + str(self.NNodeDist) + " node away.")
                break
            else:
                probeY += 1

        # 看左面
        probeX = self.GTX
        probeY = self.GTY
        while probeX >= -1:
            if probeX == -1:
                print("Nothing in left.")
                break
            if self.storedHdmap.get(probeX, probeY) is not None:
                self.WNode = self.storedHdmap.getnode(probeX, probeY)
                self.WNodeDist = probeX - self.GTX
                print("Object in left detected: " + self.WNode.landmark + ", " + str(
                    self.WNodeDist) + " node away.")
                break
            else:
                probeX -= 1

        # 看右面
        probeX = self.GTX
        probeY = self.GTY
        while probeX <= 14:
            if probeX == 14:
                print("Nothing in right.")
                break
            if self.storedHdmap.get(probeX, probeY) is not None:
                self.ENode = self.storedHdmap.getnode(probeX, probeY)
                self.ENodeDist = probeX - self.GTX
                print("Object in right detected: " + self.ENode.landmark + ", " + str(
                    self.ENodeDist) + " node away.")
                break
            else:
                probeX += 1
