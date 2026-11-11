*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  valid
    Set Password  valid12345678
    Set Password Confirmation  valid12345678
    Click  button >> text=Register
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ts
    Set Password  valid12345678
    Set Password Confirmation  valid12345678
    Click  button >> text=Register
    Registration Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  valid
    Set Password  ts34567
    Set Password Confirmation  ts34567
    Click  button >> text=Register
    Registration Should Fail With Message  Password too short

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Registration Should Fail With Message  User with username kalle already exists

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Registration Should Succeed
    Welcome Page Should Be Open

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}
