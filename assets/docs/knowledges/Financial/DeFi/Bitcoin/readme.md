[HOME](/README.md)    

---    

# Bitcoin   

## White Paper:   

![i](/assets/docs/knowledges/Financial/DeFi/Bitcoin/WhitePaper/2.png)
![i](/assets/docs/knowledges/Financial/DeFi/Bitcoin/WhitePaper/3.png)
![i](/assets/docs/knowledges/Financial/DeFi/Bitcoin/WhitePaper/4.png)
![i](/assets/docs/knowledges/Financial/DeFi/Bitcoin/WhitePaper/5.png)
![i](/assets/docs/knowledges/Financial/DeFi/Bitcoin/WhitePaper/6.png)
![i](/assets/docs/knowledges/Financial/DeFi/Bitcoin/WhitePaper/7.png)
![i](/assets/docs/knowledges/Financial/DeFi/Bitcoin/WhitePaper/8.png)
![i](/assets/docs/knowledges/Financial/DeFi/Bitcoin/WhitePaper/9.png)


---  


**detailed explanation of Bitcoin**, how it works **with the internet** and **without the internet**:

### 1. **What is Bitcoin?**
Bitcoin is a **decentralized digital currency** that enables peer-to-peer transactions without a trusted third party like a bank. It is based on **blockchain technology**, a distributed ledger that records all transactions.

Key concepts to understand about Bitcoin:
- **Blockchain**: A public ledger that records every Bitcoin transaction made. It's stored across a network of nodes (computers), ensuring transparency and security.
- **Decentralization**: Bitcoin operates on a **peer-to-peer network**, meaning there is no central authority or intermediary like a bank. Instead, users connect to the Bitcoin network directly to send and receive transactions.
- **Cryptographic Security**: Bitcoin transactions are secured using cryptography (public and private keys) to verify ownership and prevent fraud.
- **Limited Supply**: There will only ever be 21 million bitcoins, which creates scarcity and, many argue, can act as a hedge against inflation.

---

### 2. **How Bitcoin Works With the Internet**:
When you're using Bitcoin over the internet, you are interacting with the **Bitcoin network**. Here’s how the process typically works:

#### a. **Transaction Creation**:
- **Wallet**: You need a **Bitcoin wallet**, which is a software application that allows you to store and manage your bitcoins. The wallet contains your **private key** (used to sign transactions) and your **public key** (used to receive bitcoins).
- **Initiating a Transaction**: To send bitcoins, you create a transaction in your wallet. The transaction specifies:
  - The **amount** of BTC you want to send.
  - The **recipient's address** (their public key).
  - A **transaction fee** (for miners who process the transaction).
  - **Inputs**: This refers to the previous transactions (bitcoins you’ve received) that you're spending.
  
#### b. **Transaction Broadcast**:
- After creating the transaction, you sign it with your **private key** to prove ownership of the bitcoins.
- Once signed, the transaction is **broadcast** to the Bitcoin network (a distributed network of nodes). Nodes are computers running the Bitcoin protocol and maintain copies of the blockchain.
  
#### c. **Validation**:
- **Miners** (specialized nodes) group these transactions into blocks. They validate transactions to ensure:
  - The sender has enough funds to make the transaction.
  - The signatures are valid.
- Miners then compete to **mine** the block (solve a complex cryptographic puzzle). The first one to solve it adds the block to the blockchain.

#### d. **Transaction Confirmation**:
- Once the transaction is added to the blockchain, it is **confirmed**.
- The more confirmations a transaction has (i.e., more blocks are added after it), the more secure and irreversible it becomes.

#### e. **Finality**:
- After a certain number of confirmations (typically 6), the transaction is considered **final**, and the recipient can spend the bitcoins.

---

### 3. **How Bitcoin Works Without the Internet**:
Bitcoin is fundamentally designed to work over the internet, but there are ways to send or receive transactions **without direct internet access**, although these methods are more complicated and may require some intermediary solutions.

Here are some scenarios where Bitcoin can function **without the internet**:

#### a. **Offline Transactions via QR Codes**:
- **Wallets with QR Codes**: Some Bitcoin wallets can generate **QR codes** for transactions, which contain the recipient’s address and amount to send. You can use this in environments where there is no internet connection.
- **Process**:
  1. The sender creates a transaction and generates a QR code with the transaction details.
  2. The sender can then **physically show** the QR code to the recipient (through a printout, display, etc.).
  3. The recipient scans the QR code with their wallet (online or offline).
  4. The transaction is then signed offline (no internet needed), and once connected to the internet, it can be broadcast.

#### b. **SMS or Radio-based Transactions**:
- **SMS Transactions**: Some services (like **Coinapult** or **Blockstream Satellite**) allow Bitcoin transactions via **SMS**. Users can send or receive BTC through basic mobile phones (no internet needed).
  - The transaction is broadcast to the network as soon as the device has internet access, though the SMS itself is used to relay details.
  
- **Bitcoin via Radio**: In remote areas with no internet access, **radio waves** can also carry Bitcoin transactions. For example, **Blockstream Satellite** broadcasts the Bitcoin blockchain via satellite, allowing users to interact with the network without internet, using satellite dishes to receive updates and transactions.

#### c. **Air-gapped Devices (Offline Signing)**:
- **Offline Signing**: An air-gapped device is one that is **never connected to the internet**. The user can generate a Bitcoin transaction offline and sign it without exposing their private keys online.
  - **Process**:
    1. The user creates a transaction on a computer not connected to the internet (air-gapped).
    2. The unsigned transaction is transferred to an online device via a USB drive or QR code.
    3. The online device broadcasts the signed transaction to the Bitcoin network once it's connected.

This is a **high-security method** used to protect private keys from online threats, as the private key is never exposed to the internet.

---

### 4. **Challenges and Limitations of Using Bitcoin Without the Internet**:
- **Latency**: Transactions might take longer to confirm when not directly broadcast over the internet. There is always a delay between when a transaction is created and when it is confirmed on the blockchain.
- **Network Availability**: In isolated regions or during emergencies, access to Bitcoin might be severely limited without internet access.
- **Complexity**: Using Bitcoin offline (e.g., via air-gapped devices, SMS, or radio) is less user-friendly and requires additional steps and technologies compared to using Bitcoin on the internet.

---

### 5. **Bitcoin Use Cases**:
- **Investment**: People hold Bitcoin as a store of value (digital gold) and a hedge against inflation.
- **Cross-border Payments**: Bitcoin allows people to send money across borders quickly and with low fees.
- **Privacy**: Bitcoin can provide more privacy than traditional banking, though it's not fully anonymous.
- **Micropayments**: Bitcoin can facilitate small transactions that would be uneconomical through traditional financial systems.

---

### Conclusion:
- **With the Internet**: Bitcoin works via the internet by broadcasting transactions to the Bitcoin network, where they are validated, mined, and confirmed on the blockchain.
- **Without the Internet**: Bitcoin can still work through methods like **QR codes**, **SMS**, **radio-based systems**, or **offline signing**. However, these methods are slower, less user-friendly, and require additional infrastructure.

Bitcoin’s ability to function even without the internet opens doors for its use in places with limited or no access to the web, though it requires special tools and processes.

Let me know if you'd like more details on any part of this!

---    

# Raw Transaction   

A **raw Bitcoin transaction** is an unsigned or signed transaction represented in **hexadecimal format**, containing all the necessary details to be broadcast to the Bitcoin network.

Here's a quick breakdown of its structure:

1. **Version** – Indicates the transaction format version (usually `01000000` for version 1).
2. **Input count** – Number of inputs (where the BTC is coming from).
3. **Inputs**:
   - Previous transaction hash
   - Output index (vout)
   - ScriptSig (empty if unsigned)
   - Sequence number
4. **Output count** – Number of outputs (where the BTC is going).
5. **Outputs**:
   - Value in satoshis
   - ScriptPubKey (defines how the BTC can be spent)
6. **Locktime** – Optional field that specifies when the transaction can be added to the blockchain.

**Example (simplified):**
```
01000000  // version
01        // number of inputs
[...input details...]
01        // number of outputs
[...output details...]
00000000  // locktime
```

This raw transaction can be signed and then broadcast to the network using tools like Bitcoin Core or third-party APIs.

Want a real example?  

Sure! Here's a real-world example of a **raw Bitcoin transaction** in its hexadecimal format. This is a **simplified version**, as real transactions are far more complex, but it should help you understand how Bitcoin transactions are structured.

### Example Raw Transaction (Hex Format):
```
0100000001d68b276f3581b0d453da6e426aba0cc5f2f2eaf4c2b4154e1a703ea7e2be68701c000000006a473044022033f1e29b7ccf8324d3c43deccfa358340f839d1edc01d02b0e646fa8fc672b6f0220293ec8d3f4c73138d659c55cf9c0e3f5b5ed9f6ebdb6d5b08494b556c150dcf6012103f11a4e1c83f0b38fbb97e60b7c51de220625ee97175062339b0d531b3a7e9faaffffffff02b0a54b00000000001976a914c87f40a7a18e362b07f6bfa16111f4f70b1192b288ac8fa42f8d000000001976a9147ac354de2b44a31ed8ffb5f9d01812932cc705b4e88ac00000000
```

### Breakdown of the Example:

1. **Version (4 bytes)**:
   ```
   01000000
   ```
   - This indicates that the transaction follows **version 1** of the Bitcoin transaction format.

2. **Input Count (1 byte)**:
   ```
   01
   ```
   - There is **1 input** in this transaction.

3. **Input Details**:
   ```
   d68b276f3581b0d453da6e426aba0cc5f2f2eaf4c2b4154e1a703ea7e2be68701c00000000
   ```
   - The **previous transaction hash** (the transaction you are spending bitcoins from).
   - This points to the transaction that was previously created and is being used as an input for this transaction.
   
   ```
   6a
   ```
   - The length of the **ScriptSig** (a script to unlock the previous transaction). This is often a digital signature that proves you own the bitcoins being spent.
   
   ```
   473044022033f1e29b7ccf8324d3c43deccfa358340f839d1edc01d02b0e646fa8fc672b6f0220293ec8d3f4c73138d659c55cf9c0e3f5b5ed9f6ebdb6d5b08494b556c150dcf6012103f11a4e1c83f0b38fbb97e60b7c51de220625ee97175062339b0d531b3a7e9faaf
   ```
   - This is the **digital signature** (part of the ScriptSig) that proves the sender is authorized to spend the bitcoins.
   
4. **Output Count (1 byte)**:
   ```
   02
   ```
   - There are **2 outputs** in this transaction.

5. **Output 1**:
   ```
   b0a54b0000000000
   ```
   - This indicates the **amount of bitcoins** being sent (in satoshis, the smallest unit of Bitcoin). In this case, `b0a54b00` is the hexadecimal equivalent of `12000000` satoshis (0.12 BTC).

   ```
   1976a914c87f40a7a18e362b07f6bfa16111f4f70b1192b288ac
   ```
   - The **ScriptPubKey** that defines the output. This is the lock script, specifying the public key hash to which the bitcoins are sent. In this case, it's the recipient's address.

6. **Output 2**:
   ```
   8fa42f8d00000000
   ```
   - This is the amount of bitcoins being sent in the second output, `8fa42f8d` is `145000000` satoshis (1.45 BTC).

   ```
   1976a9147ac354de2b44a31ed8ffb5f9d01812932cc705b4e88ac
   ```
   - This is another **ScriptPubKey** for the second output, specifying the recipient’s public key hash for the second destination address.

7. **Locktime (4 bytes)**:
   ```
   00000000
   ```
   - This indicates that the transaction has no **locktime** (meaning it can be added to the blockchain immediately).

### Summary of This Transaction:
- **1 Input**: The bitcoins used in this transaction come from a previous transaction hash `d68b276f...`.
- **2 Outputs**: 
   - The first output sends **0.12 BTC** (120,000,000 satoshis) to a specified address (`c87f40a7...`).
   - The second output sends **1.45 BTC** (1,450,000,000 satoshis) to another address (`7ac354de...`).
- **No Locktime**: This transaction can be added to the blockchain immediately.

---

### How the Transaction Works:

1. **Input**: The sender uses an unspent transaction output (UTXO) from a previous transaction. The sender’s wallet signs the transaction with their private key, proving they own the bitcoins they want to spend.
   
2. **Transaction Broadcast**: Once signed, the transaction is broadcast to the Bitcoin network.

3. **Mining and Validation**: Miners validate the transaction, ensuring that the inputs are valid (i.e., the sender actually owns the bitcoins they’re spending). They also check that the transaction isn't a double-spend.

4. **Adding to Blockchain**: After mining, the transaction is added to the blockchain. Once confirmed, the recipient can use the newly received bitcoins.

---

### How This Relates to Real-World Usage:
When you send Bitcoin, your wallet will generate a similar raw transaction (usually in a more user-friendly format). After you sign it, your wallet will broadcast it to the Bitcoin network. Bitcoin nodes will verify the transaction before it's added to the blockchain by miners.

This example is a simplified illustration of what’s happening behind the scenes. Most users won’t directly deal with raw transactions, as wallets take care of generating, signing, and broadcasting them.

---   
