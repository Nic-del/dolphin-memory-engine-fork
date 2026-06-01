cmake_minimum_required(VERSION 3.13)

if(APPLE)
  if(DEFINED ENV{ARCHFLAGS})
    set(ARCHS "")
    if("$ENV{ARCHFLAGS}" MATCHES "x86_64")
      list(APPEND ARCHS "x86_64")
    endif()
    if("$ENV{ARCHFLAGS}" MATCHES "arm64")
      list(APPEND ARCHS "arm64")
    endif()
    if(ARCHS)
      set(CMAKE_OSX_ARCHITECTURES "${ARCHS}" CACHE STRING "" FORCE)
    endif()
  endif()
endif()

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(GCC_min_version 10)
project(dolphin-memory-engine)

if(WIN32)
    set(DolphinProcessSrc DolphinProcess/Windows/WindowsDolphinProcess.cpp)
endif(WIN32)

if(UNIX AND NOT APPLE)
   set(DolphinProcessSrc DolphinProcess/Linux/LinuxDolphinProcess.cpp)
endif(UNIX AND NOT APPLE)

if(APPLE)
   set(DolphinProcessSrc DolphinProcess/Mac/MacDolphinProcess.cpp)
endif(APPLE)

set(SRCS ${DolphinProcessSrc}
         DolphinProcess/DolphinAccessor.cpp
         Common/MemoryCommon.cpp
         MemoryWatch/MemWatchEntry.cpp
         MemoryScanner/MemoryScanner.cpp)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

add_library(dolphin-memory-engine ${SRCS})
