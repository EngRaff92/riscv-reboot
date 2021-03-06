# Disable pylint's "your name is too short" warning.
# pylint: disable=C0103

from enum import IntEnum, unique


@unique
class Instr(IntEnum):
    """Instructions where all 32 bits are fixed."""
    MRET = 0x30200073
    ECALL = 0x00000073
    EBREAK = 0x00100073


@unique
class Opcode(IntEnum):
    """Opcodes."""
    LOAD = 0b000_0011      # 0x03
    OP_IMM = 0b001_0011    # 0x13
    STORE = 0b010_0011     # 0x23
    OP = 0b011_0011        # 0x33
    BRANCH = 0b110_0011    # 0x63
    SYSTEM = 0b111_0011    # 0x73
    LUI = 0b011_0111       # 0x37
    JALR = 0b110_0111      # 0x67
    MISC_MEM = 0b000_1111  # 0x0F
    AUIPC = 0b001_0111     # 0x17
    JAL = 0b110_1111       # 0x6F

    # Opcodes in other extensions, or reserved, or custom,
    # or for other instruction lengths.
    LOAD_FP = 0b000_0111    # 0x07
    CUSTOM0 = 0b000_1011    # 0x0B
    OP_IMM32 = 0b001_1011   # 0x1B
    INSTR_48A = 0b001_1111  # 0x1F
    STORE_FP = 0b010_0111   # 0x27
    CUSTOM1 = 0b0101011
    AMO = 0b0101111
    OP32 = 0b0111011
    MADD = 0b1000011
    MSUB = 0b1000111
    NMSUB = 0b1001011
    NMADD = 0b1001111
    OP_FP = 0b1010011
    RESERVED0 = 0b1010111
    CUSTOM2 = 0b1011011
    INSTR_64 = 0b0111111
    INSTR_48B = 0b1011111
    RESERVED1 = 0b1101011
    RESERVED2 = 0b1110111
    CUSTOM3 = 0b1111011
    INSTR_80 = 0b1111111


@unique
class OpcodeSelect(IntEnum):
    """Opcode selection for state machine lookup table."""
    NONE = 0
    LOAD = 1
    STORE = 2
    OP = 3
    BRANCH = 4
    CSRS = 5
    LUI = 6
    JALR = 7
    AUIPC = 8
    JAL = 9
    OP_IMM = 10
    MRET = 11
    ECALL = 12
    EBREAK = 13


@unique
class OpcodeFormat(IntEnum):
    """Opcode formats."""
    R = 0    # OP
    I = 1    # LOAD, MISC_MEM, OP_IMM
    U = 2    # AUIPC, LUI
    S = 3    # STORE
    B = 4    # BRANCH
    J = 5    # JAL, JALR
    SYS = 6  # SYSTEM


@unique
class BranchCond(IntEnum):
    """Branch conditions."""
    EQ = 0b000
    NE = 0b001
    LT = 0b100
    GE = 0b101
    LTU = 0b110
    GEU = 0b111


@unique
class MemAccessWidth(IntEnum):
    """Memory access widths."""
    B = 0b000
    H = 0b001
    W = 0b010
    BU = 0b100
    HU = 0b101


@unique
class AluOp(IntEnum):
    "ALU card operations."
    NONE = 0b0000
    ADD = 0b0001
    SUB = 0b0010
    SLL = 0b0011
    SLT = 0b0100
    SLTU = 0b0101
    XOR = 0b0110
    SRL = 0b0111
    SRA = 0b1000
    OR = 0b1001
    AND = 0b1010
    X = 0b1011
    Y = 0b1100
    AND_NOT = 0b1101


@unique
class AluFunc(IntEnum):
    """ALU functions."""
    ADD = 0b0000
    SUB = 0b1000
    SLL = 0b0001
    SLT = 0b0010
    SLTU = 0b1011
    XOR = 0b0100
    SRL = 0b0101
    SRA = 0b1101
    OR = 0b0110
    AND = 0b0111


@unique
class SystemFunc(IntEnum):
    """System opcode functions."""
    PRIV = 0b000
    CSRRW = 0b001
    CSRRS = 0b010
    CSRRC = 0b011
    CSRRWI = 0b101
    CSRRSI = 0b110
    CSRRCI = 0b111


@unique
class PrivFunc(IntEnum):
    """Privileged functions, funct12 value."""
    # Functions for which rd and rs1 must be 0:
    ECALL = 0b000000000000
    EBREAK = 0b000000000001
    URET = 0b000000000010
    SRET = 0b000100000010
    MRET = 0b001100000010
    WFI = 0b000100000101


@unique
class TrapCause(IntEnum):
    """Trap causes."""
    INT_USER_SOFTWARE = 0x80000000
    INT_SUPV_SOFTWARE = 0x80000001
    INT_MACH_SOFTWARE = 0x80000003
    INT_USER_TIMER = 0x80000004
    INT_SUPV_TIMER = 0x80000005
    INT_MACH_TIMER = 0x80000007
    INT_USER_EXTERNAL = 0x80000008
    INT_SUPV_EXTERNAL = 0x80000009
    INT_MACH_EXTERNAL = 0x8000000B

    EXC_INSTR_ADDR_MISALIGN = 0x00000000
    EXC_INSTR_ACCESS_FAULT = 0x00000001
    EXC_ILLEGAL_INSTR = 0x00000002
    EXC_BREAKPOINT = 0x00000003
    EXC_LOAD_ADDR_MISALIGN = 0x00000004
    EXC_LOAD_ACCESS_FAULT = 0x00000005
    EXC_STORE_AMO_ADDR_MISALIGN = 0x00000006
    EXC_STORE_AMO_ACCESS_FAULT = 0x00000007
    EXC_ECALL_FROM_USER_MODE = 0x00000008
    EXC_ECALL_FROM_SUPV_MODE = 0x00000009
    EXC_ECALL_FROM_MACH_MODE = 0x0000000B
    EXC_INSTR_PAGE_FAULT = 0x0000000C
    EXC_LOAD_PAGE_FAULT = 0x0000000D
    EXC_STORE_AMO_PAGE_FAULT = 0x0000000F


@unique
class TrapCauseSelect(IntEnum):
    """Selectors for trap causes."""
    NONE = 0
    EXC_INSTR_ADDR_MISALIGN = 1
    EXC_ILLEGAL_INSTR = 2
    EXC_BREAKPOINT = 3
    EXC_LOAD_ADDR_MISALIGN = 4
    EXC_STORE_AMO_ADDR_MISALIGN = 5
    EXC_ECALL_FROM_MACH_MODE = 6
    INT_MACH_EXTERNAL = 7
    INT_MACH_TIMER = 8


@unique
class ConstSelect(IntEnum):
    """Selectors for consts."""
    EXC_INSTR_ADDR_MISALIGN = 0      # 0x00000000
    EXC_ILLEGAL_INSTR = 1            # 0x00000002
    EXC_BREAKPOINT = 2               # 0x00000003
    EXC_LOAD_ADDR_MISALIGN = 3       # 0x00000004
    EXC_STORE_AMO_ADDR_MISALIGN = 4  # 0x00000006
    EXC_ECALL_FROM_MACH_MODE = 5     # 0x0000000B
    INT_MACH_EXTERNAL = 6            # 0x8000000B
    INT_MACH_TIMER = 7               # 0x80000007
    SHAMT_0 = 8                      # 0x00000000
    SHAMT_4 = 9                      # 0x00000004
    SHAMT_8 = 10                     # 0x00000008
    SHAMT_16 = 11                    # 0x00000010
    SHAMT_24 = 12                    # 0x00000018


@unique
class CSRAddr(IntEnum):
    """CSR addresses."""
    MSTATUS = 0x300
    MIE = 0x304
    MTVEC = 0x305
    MEPC = 0x341
    MCAUSE = 0x342
    MTVAL = 0x343
    MIP = 0x344
    LAST = 0xFFF


@unique
class MStatus(IntEnum):
    """Bits for mstatus."""
    MIE = 3   # Machine interrupts global enable                  (00000008)
    MPIE = 7  # Machine interrupts global enable (previous value) (00000080)


@unique
class MInterrupt(IntEnum):
    """Bits for mie and mip."""
    MSI = 3   # Machine software interrupt enabled/pending (00000008)
    MTI = 7   # Machine timer interrupt enabled/pending    (00000080)
    MEI = 11  # Machine external interrupt enabled/pending (00000800)


@unique
class InstrReg(IntEnum):
    """Which register number to put on *_reg."""
    ZERO = 0
    RS1 = 1
    RS2 = 2
    RD = 3


@unique
class NextPC(IntEnum):
    PC_PLUS_4 = 0
    MEMADDR = 1
    Z = 2
    X = 3
    MEMADDR_NO_LSB = 4


@unique
class SeqMuxSelect(IntEnum):
    """Which input is selected in a reg/buff multiplexer card.

    For outputting to bus X, Y, or Z, if the selection is the
    same as the output bus -- that is, we send the bus to the bus itself --
    then the bus is actually disabled so that some other card can
    control the bus.

    When we want to output the trap cause or a non-MTVEC CSR to X, that's a different
    signal, which isn't handled by the mux card, so we set the selection
    to X in that case.
    """
    MEMDATA_WR = 0
    MEMDATA_RD = 1
    MEMADDR = 2
    MEMADDR_LSB_MASKED = 3
    PC = 4
    PC_PLUS_4 = 5
    MTVEC = 6
    MTVEC_LSR2 = 7
    TMP = 8
    IMM = 9
    INSTR = 10
    X = 11
    Y = 12
    Z = 13
    Z_LSL2 = 14
    CONST = 15
