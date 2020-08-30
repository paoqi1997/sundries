#ifndef PQLIB_CORE_H
#define PQLIB_CORE_H

#include <cstdio>
#include <iostream>

namespace pqlib
{

/**
 * @brief Socket对象
 */
class Socket
{
public:
    Socket() : sockfd(-1), type("nil")
    {
        std::cout << "Socket::Socket" << std::endl;
    }
    Socket(int fd, const char *_type) : sockfd(fd), type(_type)
    {
        std::printf("Socket::Socket(%d, \"%s\")\n", fd, _type);
    }
    virtual ~Socket()
    {
        std::cout << "Socket::~Socket" << std::endl;
    }
    /**
     * @brief 获取文件描述符
     * @return 文件描述符
     */
    int getFd() const { return sockfd; }
    /**
     * @brief 设置文件描述符
     * @param fd 文件描述符
     */
    void setFd(int fd) { sockfd = fd; }
    /**
     * @brief 获取socket类型
     * @return socket类型
     */
    const char* getType() const { return type; }
private:
    int sockfd;
    const char *type;
};

/**
 * @brief 面向TCP连接的Socket对象
 */
class TcpSocket : public Socket
{
public:
    TcpSocket()
    {
        std::cout << "TcpSocket::TcpSocket" << std::endl;
    }
    TcpSocket(int sockfd) : Socket(sockfd, "tcp")
    {
        std::printf("TcpSocket::TcpSocket(%d)\n", sockfd);
    }
    ~TcpSocket()
    {
        std::cout << "TcpSocket::~TcpSocket" << std::endl;
    }
};

} // namespace pqlib

#endif // PQLIB_CORE_H
