# build stage
FROM openjdk:17-jdk-alpine AS build
WORKDIR /land
# 도커파일이 위치한 곳의 파일을 현위치에 카피
COPY . .
RUN ./gradlew clean bootJar

# run stage
FROM eclipse-temurin:17-jre-alpine AS run
COPY --from=build /land/build/libs/*.jar app.jar
ENTRYPOINT ["java","-jar","/app.jar"]
