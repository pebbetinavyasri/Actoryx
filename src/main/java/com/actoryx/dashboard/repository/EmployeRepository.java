package com.actoryx.dashboard.repository;

import com.actoryx.dashboard.model.Employee;
import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface EmployeRepository extends MongoRepository<Employee, String> {
}